FROM python:3.7

# 모든 파일을 컨테이너의 /app 디렉토리에 복사한다.
COPY ./ /app

# 작업 디렉토리를 설정한다.
WORKDIR /app

# pip를 업그레이드하고 필요한 패키지들을 설치한다.
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn[standard] tensorflow torch

# 8000 포트를 외부로 노출시킨다.
EXPOSE 8000

# Uvicorn을 사용하여 앱을 시작하는 명령어를 설정한다.
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
