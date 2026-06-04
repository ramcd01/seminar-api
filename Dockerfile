# 파이썬 3.12 슬림 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치 (MariaDB 커넥터 등 빌드 시 필요)
RUN apt-get update && apt-get install -y \
    build-essential \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 소스 코드 복사
COPY . .

# Gunicorn을 사용하여 Flask 앱 실행
# app:app은 app/__init__.py의 flask 객체를 의미
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
