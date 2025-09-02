# Week 3 Auth API — curl Cheatsheet (JSON)

## 1️⃣ Signup

```bash
curl -X POST http://127.0.0.1:8000/api/v1/signup \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"secret123"}'
```

## 2️⃣ Login

```bash
curl -X POST http://127.0.0.1:8000/api/v1/login \
  -F "username=testuser" \
  -F "password=secret123"
```

**Response Example:**

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

## 3️⃣ Access Protected Route

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" \
  http://127.0.0.1:8000/api/v1/protected
```

- Replace `<JWT_TOKEN>` with the token from login.  
- Returns 401 Unauthorized if missing or invalid.

## 4️⃣ Using a Shell Variable for Token

```bash
TOKEN=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username":"testuser","password":"secret123"}' http://127.0.0.1:8000/api/v1/login | jq -r .access_token)

curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/api/v1/protected
```

> `jq` parses JSON output to extract the access token automatically.

## 5️⃣ Quick Tips

- Always use **POST** for `/signup` and `/login` endpoints.  
- Use `/docs` (Swagger UI) for interactive testing.  
- Ensure `python-multipart` is installed only if you switch to Form(...) endpoints.
