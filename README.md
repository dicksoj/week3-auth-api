# Week 3 — Auth API

A minimal FastAPI project with JWT authentication, protected routes, OpenAPI docs, CI pipeline, and Docker image publishing to **GitHub Container Registry (GHCR)**.

---

## 🚀 Features

- **JWT Auth** — signup & login with password hashing (passlib) and JWT tokens (python-jose).  
- **Protected Routes** — `/api/v1/todos/*` requires valid JWT.  
- **OpenAPI Docs** — tagged endpoints, versioned under `/api/v1`.  
- **CI/CD** — GitHub Actions pipeline for linting, testing, and pushing Docker image.  
- **GHCR Publishing** — image available at `ghcr.io/<your-username>/auth-api:latest`.

---

## 📂 Project Structure

```
week3-auth-api/
├── app/
│   ├── main.py            # FastAPI app entry
│   ├── auth.py            # JWT auth logic (signup, login, password hashing)
│   ├── models.py          # Pydantic models
│   └── todos.py           # Protected routes
├── tests/
│   └── test_auth.py       # Basic tests for auth
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Local dev setup
├── requirements.txt       # Python dependencies
├── Makefile               # Common dev/CI commands
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions CI pipeline
```

---

## 🛠️ Development with Makefile

Run common tasks with `make`:

```bash
make build    # Build Docker images
make up       # Start containers
make down     # Stop containers
make logs     # Follow logs
make test     # Run pytest
make lint     # Run flake8
make push     # Build & push image to GHCR
```

> Replace `<your-username>` in the `push` target with your GitHub username.

---

## ⚡ Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

Visit:
- Swagger docs → http://127.0.0.1:8000/docs  
- Signup/Login → `/api/v1/signup`, `/api/v1/login`  
- Protected route → `/api/v1/todos/*`  

---

## 📦 Docker

### Build & Run

```bash
docker build -t week3-auth-api .
docker run -p 8000:8000 week3-auth-api
```

### Publishing to GHCR

1. Create a GitHub Personal Access Token (PAT) with **`write:packages`** scope.  
2. Authenticate with GHCR:
```bash
echo $CR_PAT | docker login ghcr.io -u <your-username> --password-stdin
```
3. Push image using Makefile:
```bash
make push
```
4. Pull image anywhere:
```bash
docker pull ghcr.io/<your-username>/auth-api:latest
```

---

## 📜 CI/CD with GitHub Actions

The workflow (`.github/workflows/ci.yml`) runs on push/PR to `main`:

- Installs dependencies  
- Runs **lint** + **tests**  
- Builds & pushes Docker image to **GHCR**

