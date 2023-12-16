# 인공지능 기반 한국어 비속어 필터링

인공지능을 기반으로 하여 문장의 비속어를 파악하는 HTTP API

음소, 음절별로 문장을 분해하여 인공지능을 통해 비속어 여부를 분석할 수 있습니다.

## ❗️ 변경 사항

이 프로젝트는 [원본 프로젝트](https://github.com/hjh010501/appropriate-filetering)를 기반으로 하고 있습니다.

[원본 프로젝트](https://github.com/hjh010501/appropriate-filetering)와 비교하여 다음과 같은 주요 변경 사항이 있습니다:

- FastAPI 사용: Flask에서 FastAPI로 전환하였습니다. 이를 위해 모든 라우팅과 요청 처리 로직을 FastAPI 스타일로 재작성하였습니다. 또한 요청 url및 응답 형태를 변경하였습니다.
- Dockerfile 수정: Dockerfile의 Python 환경 설정 부분을 FastAPI와 호환되도록 업데이트하였으며, TensorFlow를 포함하는 필요한 패키지들을 설치하도록 변경하였습니다.
- Index.html 및 이미지 제거: 문장 내에 있는 비속어 필터링하는 페이지를 미제공하도록 수정하였습니다.

## 🛠️ 프로젝트 개발 환경

프로젝트는 아래 환경에서 개발되었습니다.

> OS: macOS Sonoma   
> IDE: Pycharm  
> Python: 3.11.6

## ✅ 프로젝트 개발/실행

해당 프로젝트를 추가로 개발 혹은 실행시켜보고 싶으신 경우 아래의 절차에 따라 진행해주세요

#### 1. 가상 환경 생성

```commandline
python3 -m venv venv
```

#### 2. 가상 환경 활성화

```commandline
source venv/bin/activate
```

#### 3. requirements 다운로드

```commandline
pip install -r requirements.txt
```

#### 4. 프로그램 실행

```commandline
uvicorn api:app --port 8000 --reload
```

**참고) 프로젝트가 실행 중인 환경에 한해 아래 URL에서 API 명세서를 확인할 수 있습니다**

```commandline
http://localhost:8000/docs
http://localhost:8000/redoc
```
