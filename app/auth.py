from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .models import UserCreate, Token

router = APIRouter(tags=["auth"])

SECRET_KEY = "super-secret"   # load from env in real app
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

users_db = {}  # in-memory store

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def hash_password(password):
    return pwd_context.hash(password)

def create_token(data: dict, expires_delta=None):
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode = {**data, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup", response_model=dict, summary="Register a new user")
def signup(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(400, "User already exists")
    users_db[user.username] = hash_password(user.password)
    return {"msg": "User created"}

@router.post("/login", response_model=Token, summary="Login and get JWT")
def login(form: OAuth2PasswordRequestForm = Depends()):
    hashed = users_db.get(form.username)
    if not hashed or not verify_password(form.password, hashed):
        raise HTTPException(401, "Invalid credentials")
    token = create_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/protected", summary="Protected route")
def protected(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"msg": f"Hello {payload['sub']}, you are authorized!"}
    except JWTError:
        raise HTTPException(403, "Invalid or expired token")

