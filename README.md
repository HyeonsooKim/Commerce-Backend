# 레포지토리 명
비밀번호 적용 자유 게시판

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [개발 인원](#개발-인원)
5. [API 목록](#API-목록)


<br>


## 프로젝트 개요
- 게시판 구현(CRUD)
- 게시글 수정 및 삭제 시 비밀번호 인증
- 비밀번호 조건(6자리 이상, 숫자 1자리 이상)
- 접속 IP 및 작성시간 기반 날씨 API 적용
- Pagination

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
- 2022/09/08~2022/09/14


<br>


## 팀 구성
| 김현수 |
| ------ |
| [Github](https://github.com/HyeonsooKim)


<br>


## ERD
ERD 


<br>
<img width="783" alt="스크린샷 2022-09-14 오후 11 58 04" src="https://user-images.githubusercontent.com/48047773/190190791-534c24d4-a531-4740-ba10-30ce42f526a4.png">


## API 목록
API 명세 주소

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
