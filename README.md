# 레포지토리 명
쇼핑몰 백엔드 기능 구현

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [개발 인원](#개발-인원)
5. [API 목록](#API-목록)


<br>


## 프로젝트 개요
- 유저/상품/주문 CRUD 기능
- 주문 username으로 검색 기능
- 지정 날짜 및 날짜 범위 내 주문 필터링 기능
- 주문 상태 및 배송 상태별 필터링 기능
- 쿠폰 시스템(추가 예정)

<br>

## 프로젝트 기술 스택

### Backend
<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB
<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools
<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-5865F2?logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
</section>
<!-- | 백엔드 | DB   |  Tools   |
| ---- | ------ | --- |
|      |        |    | -->


<br>


## 개발 기간
- 2022/09/06~2022/09/07


<br>


## 개발 인원
| 김현수 |
| ------ |
| [Github](https://github.com/HyeonsooKim) |


<br>


## 개발 기간
- 2022/09/08~2022/09/15


<br>


## 팀 구성
| 김현수 |
| ------ |
| [Github](https://github.com/HyeonsooKim)


<br>


## ERD
ERD 
<img width="805" alt="스크린샷 2022-09-15 오후 11 26 11" src="https://user-images.githubusercontent.com/48047773/190429884-51722947-5eda-4822-a956-4adceaec4f55.png">


<br>
<img width="783" alt="스크린샷 2022-09-14 오후 11 58 04" src="https://user-images.githubusercontent.com/48047773/190190791-534c24d4-a531-4740-ba10-30ce42f526a4.png">


## API 목록
API 명세 주소
![127 0 0 1_8000_api_swagger (1)](https://user-images.githubusercontent.com/48047773/190426782-7eb1b15e-6d28-4629-97f7-f2ed4f44526a.png)

<br>


## 프로젝트 시작 방법
1. 로컬에서 실행할 경우
```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch ${github 주소}
cd ${디렉터리 명}

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>

