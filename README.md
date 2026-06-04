# Seminar Room Reservation API

Flask와 MariaDB를 활용한 세미나룸 예약 관리 RESTful API 서버입니다. Docker 환경에서 구동되며, GitHub Actions를 통한 CI(지속적 통합) 환경이 구축되어 있습니다.

---

## 🚀 프로젝트 개요

세미나룸 정보 및 예약 현황을 효율적으로 관리하기 위한 RESTful API입니다.

Docker Compose를 사용하여 별도의 복잡한 DB 설정 없이 개발 및 실행 환경을 빠르게 구축할 수 있으며, GitHub Actions를 통해 자동 테스트가 수행됩니다.

---

## 🛠 기술 스택

### Backend

* Python 3.12
* Flask
* Gunicorn

### Database

* MariaDB 10.6
* mysql-connector-python

### Infrastructure & DevOps

* Docker
* Docker Compose
* GitHub Actions

---

## 📂 프로젝트 구조

```text
seminar-api/
├── app/                 # 메인 애플리케이션 (routes, db, config)
├── migrations/          # DB 초기화 SQL 스크립트
├── tests/               # pytest 기반 단위 테스트
├── Dockerfile           # Flask 컨테이너 이미지 빌드 설정
├── docker-compose.yml   # DB 및 서비스 오케스트레이션
└── requirements.txt     # 의존성 패키지 목록
```

---

## ⚙️ 브랜치 전략

| 브랜치    | 역할                    |
| ------ | --------------------- |
| `main` | 배포용 브랜치               |
| `devA` | API 및 DB 개발           |
| `devB` | Docker 인프라 및 CI/CD 구축 |

### Workflow

1. 기능별 브랜치에서 개발 진행
2. Pull Request 생성
3. 코드 리뷰 및 테스트 수행
4. `main` 브랜치로 병합

---

## 🚀 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/gyagoooooo/prac-seminar-api.git
cd prac-seminar-api
```

### 2. 컨테이너 실행

```bash
docker compose up -d --build
```

### 3. 상태 확인

```bash
docker ps
```

다음 컨테이너가 정상적으로 실행 중인지 확인합니다.

* `seminar_api`
* `seminar_db`

---

## 📡 API 명세

| 기능      | 메서드    | 엔드포인트                    | 비고           |
| ------- | ------ | ------------------------ | ------------ |
| 헬스 체크   | GET    | `/health`                | 서버 상태 확인     |
| 룸 전체 조회 | GET    | `/api/rooms`             | 전체 세미나룸 조회   |
| 룸 등록    | POST   | `/api/rooms`             | JSON Body 필요 |
| 예약 조회   | GET    | `/api/reservations`      | 쿼리 파라미터 지원   |
| 예약 등록   | POST   | `/api/reservations`      | 예약 생성        |
| 예약 취소   | DELETE | `/api/reservations/{id}` | 예약 삭제        |

> 상세 요청(Request) 및 응답(Response) 예시는 Wiki를 참고하세요.

---

## 🧪 테스트

프로젝트는 `pytest`를 사용하여 API 테스트를 수행합니다.

### 로컬 테스트 실행

```bash
pytest tests/test_api.py
```

### CI 자동 테스트

GitHub Actions가 설정되어 있어 `main` 브랜치로 Push 또는 Pull Request 시 자동으로 테스트가 실행됩니다.

---

## 📦 데이터베이스 영속성

Docker Volume을 사용하여 데이터베이스를 영구 저장합니다.

* Volume 이름: `seminar_data`
* 컨테이너 재시작 시 데이터 유지
* 컨테이너 삭제 후에도 데이터 보존

---

## 👥 개발 환경

| 항목         | 환경                         |
| ---------- | -------------------------- |
| OS         | Windows 11 / WSL2 (Ubuntu) |
| Database   | MariaDB 10.6               |
| Language   | Python 3.12                |
| Web Server | Gunicorn                   |
