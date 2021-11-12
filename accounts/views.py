from rest_framework             import viewsets, status
from rest_framework.decorators  import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework.pagination  import CursorPagination
from django_filters             import utils

from accounts.managers import AccountManager
from accounts.models   import Account, TradeLog
from .serializers      import TradeLogSerializer
from .filters          import TradeLogListFilter
from accounts.models import Account, TradeLog
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        계좌생성
        POST /accounts/

        data params
        - name
        - number
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = Account.objects.create(
            name=request.data.get('name'),
            number=request.data.get('number'),
            user=request.user
        )
        return Response(self.get_serializer(account).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        계좌 리스트 조회
        GET /accounts/
        """
        accounts = Account.objects.filter(user=request.user).all()
        return Response(self.get_serializer(accounts, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def deposit(self, request, pk):
        """
        입금
        POST /accounts/{account_id}/deposit/
        """
        manager = AccountManager()
        account = manager.get_account(request.user, pk)
        account, trade_log = manager.deposit(account, request.data)
        # todo: 성공 리스폰스 처리
        return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def withdrawal(self, request, pk):
        """
        출금
        POST /accounts/{account_id}/withdrawal/
        """
        manager = AccountManager()
        account = manager.get_account(request.user, pk)
        account, trade_log = manager.withdrawal(account, request.data)
        # todo: 성공 리스폰스 처리
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def tradelogs(self, request, pk):
        """
        계좌 리스트 조회
        GET /accounts/{account_id}/tradelogs/
        """
        tradelogs = TradeLog.objects.filter(account_id=pk)

        filter_set = {
            'data': request.query_params,
            'queryset': tradelogs,
            'request': request,
        }

        filterset = TradeLogListFilter(**filter_set)

        if not filterset.is_valid() and self.raise_exception:
            raise utils.translate_validation(filterset.errors)

        cursorPaginator = CursorPagination()
        cursorPaginator.page_size = 20

        ordering_filter = {'desc': '-created_at', 'asc': 'created_at'}
        cursorPaginator.ordering = ordering_filter.get(filter_set['data'].get('order'), '-created_at')

        paginated_tradelogs = cursorPaginator.paginate_queryset(filterset.qs, request)
        result = TradeLogSerializer(paginated_tradelogs, many=True)

        return cursorPaginator.get_paginated_response(result.data)
