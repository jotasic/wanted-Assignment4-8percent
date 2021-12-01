# Assignment4

원티드x위코드 백엔드 프리온보딩 과제4
- 과제 출제 기업 정보
  - 기업명 : 8퍼센트
  -  [8퍼센트 사이트](https://8percent.kr/)
  - [원티드 채용 링크](https://www.wanted.co.kr/wd/64695)

## 과제 후기
- https://velog.io/@burnkim61/프리온보딩-과제-4

## 팀 Repository
- https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment4

## Members
|이름   |github                   |담당 기능|
|-------|-------------------------|--------------------|
|김태우 |[jotasic](https://github.com/jotasic)       | API(거래내역)                           |
|고유영 |[lunayyko](https://github.com/lunayyko)     | API(회원가입, 로그인, 로그아웃), 배포환경설정  |
|박지원 |[jiwon5304](https://github.com/jiwon5304)   | API(회원가입, 로그인, 로그아웃)             |
|최신혁 |[shchoi94](https://github.com/shchoi94)     | API(계좌생성, 계좌목록조회, 입금, 출금), swagger 세팅|
|박세원 |[sw-develop](https://github.com/sw-develop) | API(거래내역), Functional Test         |

## 과제 내용

<details>
  <summary><b>과제 내용 자세히 보기</b></summary>
<div markdown="1">
	
### [필수 포함 사항]

- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

> 📝 “계좌 거래 API”를 구현해주세요. API는 3가지가 구현되어야 합니다.


 **✔️ API 목록**
---
- 거래내역 조회 API
- 입금 API
- 출금 API

**✔️ 주요 고려 사항은 다음과 같습니다.**
---
- 계좌의 잔액을 별도로 관리해야 하며, 계좌의 잔액과 거래내역의 잔액의 무결성의 보장
- DB를 설계 할때 각 칼럼의 타입과 제약

**✔️ 구현하지 않아도 되는 부분은 다음과 같습니다.**
- 문제와 관련되지 않은 부가적인 정보. 예를 들어 사용자 테이블의 이메일, 주소, 성별 등
- 프론트앤드 관련 부분

**✔️  제약사항은 다음과 같습니다.**
- (**8퍼센트가 직접 로컬에서 실행하여 테스트를 원하는 경우를 위해**) 테스트의 편의성을 위해 mysql, postgresql 대신 sqllite를 사용해 주세요.

**✔️  상세설명**
**1)** 거래내역 조회 **API**

- 아래와 같은 조회 화면에서 사용되는 API를 고려하시면 됩니다.
    

거래내역 API는 다음을 만족해야 합니다.
- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 거래일시에 대한 필터링이 가능해야 합니다.
- 출금, 입금만 선택해서 필터링을 할 수 있어야 합니다.
- Pagination이 필요 합니다.
- 다음 사항이 응답에 포함되어야 합니다.
    - 거래일시
    - 거래금액
    - 잔액
    - 거래종류 (출금/입금)
    - 적요

**2)** 입금 **API**

입금 API는 다음을 만족해야 합니다.
- 계좌의 소유주만 요청 할 수 있어야 합니다.

**3)** 출금 **API**
출금 API는 다음을 만족해야 합니다.
- 계좌의 소유주만 요청 할 수 있어야 합니다.
- 계좌의 잔액내에서만 출금 할 수 있어야 합니다. 잔액을 넘어선 출금 요청에 대해서는 적절한 에러처리가 되어야 합니다.

**4)** 가산점
다음의 경우 가산점이 있습니다.
- Unit test의 구현
- Functional Test 의 구현 (입금, 조회, 출금에 대한 시나리오 테스트)
- 거래내역이 1억건을 넘어갈 때에 대한 고려
    - 이를 고려하여 어떤 설계를 추가하셨는지를 README에 남겨 주세요.
	
	</details>

## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/sqlite-0064a5?style=for-the-badge&logo=sqlite&logoColor=white"/>&nbsp;
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/SWAGGER-5B8C04?style=for-the-badge&logo=Swagger&logoColor=white"/>&nbsp;

## 모델링
![image](https://user-images.githubusercontent.com/8219812/141481348-01525848-e996-4477-9b1f-e1a63ed016a2.png)

- 계좌잔액, 거래내역의 금액 관련 필드들 일반 IntegerField 대신, PositiveBigIntegerField를 사용하였습니다.
- IntegerField는 약 21억까지 저장되기 때문에, 계좌 잔액을 나타내기가 부족하다고 판단했습니다. BigIntegerField로 할 시, 약 900경까지 표현할 수 있습니다.

## API
[링크-Swagger](http://18.188.189.173:8031/swagger/)

## 구현 기능

**1. 거래 내역 조회 API** - 🙋‍♂️ 담당기능
  - 계좌의 소유주만 거래 내역 조회 가능
  - 입금, 출금만 선택해서 필터링
  - 거래일시별로 조회기간을 정해서 필터링, Pagination	
	
**2. 회원가입, 로그인, 로그아웃**
 - 커스텀 유저모델 생성, username 대신 email을 사용
 - rest_auth 사용, 로그인 시 토큰 생성

**3. 입급, 출금 API**
 - 계좌의 소유주만 계좌에서 입금, 출금 
 - 잔액을 넘어서 출금 요청을 하면 에러 메세지 반환

**4. 계좌 생성 및 계좌List API**
- 로그인한 유저만 접근 및 생성 가능
- 자신의 계좌만 List로 보여준다.


## 거래내역이 1억건을 넘어갈 때에 대한 고려
### 개요
약 500만개의 거래내역을 기반으로 성능 테스트를 하였습니다

### DB Index 적용

거래정보 테이블에서 색인에 자주 사용하는 account와 created_at의 index를 지정하였습니다.
```python
class TradeLog(models.Model): 

    account     = models.ForeignKey(.....db_index=True)
		...
    created_at  = models.DateTimeField(....db_index=True)
```

### 캐시 사이즈 늘리기
sqlite 캐시 사이즈를 늘려봤습니다.
    
    ```bash
    def activate_db_optimize(sender, connection, **kwargs):
        """Enable integrity constraint with sqlite."""
        if connection.vendor == 'sqlite':
            cursor = connection.cursor()
            cursor.execute('PRAGMA cache_size = 100000;')
    
    connection_created.connect(activate_db_optimize)
    ```
    
 장고 쉘에서는 약 500만건의 data의 count를 측정할 때, 성능 차이가 있었습니다. 약 10배)
    
    ```bash
    # 캐시 적용 안함
    In [3]: TradeLog.objects.count()
    Time: 0.07888481 s
    SQL: SELECT COUNT(*) AS "__count" FROM "trade_logs"
    Args: ()
    Out[3]: 5849542
    
    # 캐시 적용
    In [7]: TradeLog.objects.count()
    Time: 0.00876825 s
    SQL: SELECT COUNT(*) AS "__count" FROM "trade_logs"
    Args: ()
    Out[7]: 5849542
    ```
    
  하지만 실제 api 호출에서는 성능은 하락하였습니다.
  
  **캐시 적용 안함 - 571ms**
  ![캐시적용 안함](https://user-images.githubusercontent.com/8219812/141517870-d5049776-dae4-441c-9f1f-a65ee5ecf175.png)

  **캐시 적용 - 651ms**
  ![캐시적용](https://user-images.githubusercontent.com/8219812/141517882-7016cb09-0638-4705-a667-e51124b2e071.png)

    
### Cursor Pagnation 적용
  - Cursor Pagnation은 다음 페이지네이션의 PK를 기반으로 페이지를 구하는 방식을 말합니다.
      - 인덱스가 적용된 값을 비교하기 때문에 테이블 풀스캔을 하지 않습니다.
      - id 값으로 데이터를 조회하기 때문에, 데이터 쓰기가 빈번한 테이블이여도 다음 페이지네이션 조회 시 값이 누락되지 않습니다.
  - 반면 limit&offset pagination은 offset 위치를 계산하고, 필요한 데이터를 찾을 때까지 테이블을 전체 스캔하므로 offset이 커질 수록 DB 부하 리스크는 더 커집니다.


하지만 실제 api 호출에서는 limit&offset 보다 성능이 하락하였습니다.

**Cursor Pagnatio - 571msn**
  ![캐시적용 안함](https://user-images.githubusercontent.com/8219812/141517870-d5049776-dae4-441c-9f1f-a65ee5ecf175.png)

**limit&offset pagination - 171ms**
  ![스크린샷 2021-11-13 오전 3 24 04](https://user-images.githubusercontent.com/8219812/141518278-2606467f-0ec5-461c-b8b2-894c012530a5.png)

### 정리
- 결론적으로는 거래내역이 1억건을 넘어갈 때에 어떻게 하면 효율 적으로 할 수 있는지 대안을 제시 못하였습니다.
- 이론과 다르게 테스트 한 방식이 잘못되어 잘못된 결과가 나왔는지 아니면 어떠한 이유가 있어서 이러한 결과가 나왔는지 추후에 자료들을 더 찾아봐야 될 것 같습니다

## Functional Test 의 구현 시나리오
- Functional Test는 E2E(End-to-End) 혹은 브라우저 테스트로 소프트웨어 내부 구조나 구현 방법을 고려하기보다 테스트 시나리오를 바탕으로 실제 사용자가 접하는 브라우저 테스트를 하는 것입니다.
- 하지만 현재 프로젝트는 프론트 부분을 구현하지 않았으므로 해당 방향으로 테스트를 진행하기는 어렵다고 판단하였습니다.
- 대신 사용자의 입장에서 구현한 기능(회원가입/로그인/계좌 및 거래 관련)들의 일련의 시나리오를 각각 구성하여 테스트를 진행하였으며, 핵심 기능인 입금, 출금, 거래 내역 조회 시나리오는 다음과 같습니다.

**입금 시나리오**
  - 사용자 로그인 → 계좌 생성 → 입금 → 입금 거래 내역 조회 에 대한 테스트 시나리오를 작성 하였고, 현재 계좌의 잔액과 마지막 입금 내역의 잔액이 동일함을 확인하여 테스트를 통과하였다. (테스트 시나리오에서 진행한 입금이 마지막 거래 내역이라고 가정)

**출금 시나리오**
  - 로그인 → 출금 → 출금 거래 내역 조회 에 대한 테스트 시나리오를 작성하였고, 현재 계좌의 잔액과 마지막 출금 내역의 잔액이 동일함을 확인하여 테스트를 통과하였다. (테스트 시나리오에서 진행한 출금이 마지막 거래 내역이라고 가정)
 
**거래 내역 조회 시나리오**
   - 로그인 → 입금/출금 내역 생성 → 거래 내역 조회 에 대한 테스트 시나리오를 작성하였고, 생성한 거래 내역(2개)을 기반으로 ‘조회 기간‘이 오늘이고, ‘최근 거래 내역이 위로’인 경우에 대한 응답으로 온 거래 내역 데이터가 총 2개이고, 현재 계좌의 잔액과 마지막 거래 내역의 잔액이 동일함을 확인하여 테스트를 통과합니다.

위의 시나리오를 [test_functional_test.py](./test_functional_test.py)에 구현하였습니다.



## 배포정보
---
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 | http://18.188.189.173:8031/            |    |


## API TEST 방법
1. 우측 링크를 클릭해서 swagger로 들어갑니다. [링크](http://18.188.189.173:8031/swagger/)

2. 회원가입을 진행합니다. (email, name, password 필드만 입력)
![image](https://user-images.githubusercontent.com/8219812/141522562-3af590c5-fe35-4ca6-a421-d03e8a01b51c.png)

3. 가입된 정보를 이용해서 로그인을 합니다. (email, password 필드만 입력)
![image](https://user-images.githubusercontent.com/8219812/141519922-ba5273b4-8684-4ee4-8926-8a93611dd5ef.png)

4. 로그인 시 획득한 access key를 이용해서 다른 api에 적용합니다.
![image](https://user-images.githubusercontent.com/8219812/141520154-6fcd99ab-81cf-4e14-9ac0-0c1e5fb8f6cb.png)

다른 api의 Authorization 항목에 `Token access_key` 를 입력합니다.
![image](https://user-images.githubusercontent.com/8219812/141520314-76c28e9c-8e96-4d1c-b08f-1960eda2b8c0.png)


## 설치 및 실행 방법
	
<details>
  <summary><b>설치 및 실행 방법 자세히 보기</b></summary>
<div markdown="1">	
	
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment4
    cd Assignment4
    ```

2. 가상 환경을 만들고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create --name Assignment4 python=3.8
    conda actvate Assignment4
    pip install -r requirements.txt
    ```

3. Django SECRET_KEY용 환경 변수를 등록한다.
   ```bash
      export DJANGO_SECRET_KEY='django시크릿키'
    ```

4. db를 table 구조를 최신 model에 맞게 설정한다.
    ```bash
    python manage.py migrate
    ```

5. 서버를 실행한다.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

###  배포용 
1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment4
    cd Assignment4
    ```

2. docker환경 설정 파일을 만든다.

  
3. 백엔드 서버용 .dockerenv.deploy.backend 파일을 만들어서 안에 다음과 같은 내용을 입력한다. manage.py와 같은 폴더에 생성한다.
    ### .dockerenv.deploy.backend
    ```text
      DJANGO_SECRET_KEY='django시크릿키'
    ```
       
4. docker-compose를 통해서 db와 서버를 실행시킨다.
    
    ```bash
    docker-compose -f docker-compose-deploy.yml up
    ```
    
5. 만약 백그라운드에서 실행하고 싶을 시 `-d` 옵션을 추가한다.
  
    ```bash
    docker-compose -f docker-compose-deploy.yml up -d
    ```

</details>
	
## 폴더 구조

```bash
📦Assignment4
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜tests_account.py
 ┃ ┃ ┣ 📜tests_deposit.py
 ┃ ┃ ┣ 📜tests_tradelog.py
 ┃ ┃ ┗ 📜tests_withdrawal.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜exceptions.py
 ┃ ┣ 📜filters.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂config
 ┃ ┗ 📂nginx
 ┃ ┃ ┗ 📜nginx.conf
 ┣ 📂eight_percent
 ┃ ┣ 📂settings
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜deploy.py
 ┃ ┃ ┣ 📜dev_local.py
 ┃ ┃ ┗ 📜dev_local_dblog.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂users
 ┃ ┣ 📂migrations
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📜docker-compose-depoly.yml
 ┣ 📜README.md
 ┣ 📜manage.py
 ┣ 📜pull_request_template.md
 ┣ 📜requirements.txt
 ┗ 📜test_functional_test.py
```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 8퍼센트에서 출제한 과제를 기반으로 만들었습니다.
