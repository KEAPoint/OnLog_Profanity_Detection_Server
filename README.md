# 인공지능 기반 한국어 비속어 필터링

인공지능을 기반으로 하여 문장의 비속어를 파악하는 HTTP API

음소, 음절별로 문장을 분해하여 인공지능을 통해 비속어 여부를 분석할 수 있습니다.

## 변경 사항
이 프로젝트는 [원본 프로젝트](https://github.com/hjh010501/appropriate-filetering)를 기반으로 하고 있습니다.

[원본 프로젝트](https://github.com/hjh010501/appropriate-filetering)와 비교하여 다음과 같은 주요 변경 사항이 있습니다:
- FastAPI 사용: Flask에서 FastAPI로 전환하였습니다. 이를 위해 모든 라우팅과 요청 처리 로직을 FastAPI 스타일로 재작성하였습니다. 또한 요청 url및 응답 형태를 변경하였습니다.
- Dockerfile 수정: Dockerfile의 Python 환경 설정 부분을 FastAPI와 호환되도록 업데이트하였으며, TensorFlow를 포함하는 필요한 패키지들을 설치하도록 변경하였습니다.
- Index.html 및 이미지 제거: 문장 내에 있는 비속어 필터링하는 페이지를 미제공하도록 수정하였습니다. 
- github action 사용: 변경된 파일에 맞는 이미지를 생성하고자 github action을 통해 docker hub에 배포하도록 수정하였습니다. [Dockerfile](Dockerfile)