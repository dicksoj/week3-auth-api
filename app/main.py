from fastapi import FastAPI
from . import auth

app = FastAPI(
    title="Auth API",
    description="JWT Authentication demo with protected routes",
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "Signup/Login"},
        {"name": "protected", "description": "Protected resources"},
    ],
)

app.include_router(auth.router, prefix="/api/v1")

