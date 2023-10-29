# Docker Hub에서 공식 Python 이미지를 가져옵니다.
FROM python:3.7

# 모든 파일을 컨테이너의 /app 디렉토리에 복사합니다.
COPY ./ /app

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# pip를 업그레이드하고 필요한 패키지들을 설치합니다.
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn[standard] tensorflow torch

# 8000 포트(기본적으로 FastAPI가 이 포트에서 실행됩니다)를 외부로 노출시킵니다.
EXPOSE 8000

# Uvicorn을 사용하여 앱을 시작하는 명령어를 설정합니다.
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
