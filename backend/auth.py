from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import SessionLocal
import secrets
import string


# Security configuration
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  # Fixed key - change in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Bearer token scheme
security = HTTPBearer()

def generate_client_id() -> str:
    """Generate a unique client ID"""
    random_part = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(12))
    return f"CL_{random_part}"

def generate_client_key() -> str:
    """Generate a secure client key"""
    random_part = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
    return f"CK_{random_part}"

def verify_client_key(plain_key: str, hashed_key: str) -> bool:
    """Verify a client key against its hash"""
    return pwd_context.verify(plain_key, hashed_key)

def get_client_key_hash(client_key: str) -> str:
    """Hash a client key"""
    return pwd_context.hash(client_key)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """Decode and validate a JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_current_client(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Dependency to get the current authenticated client"""
    from models import Client
    
    db = SessionLocal()
    
    try:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        token = credentials.credentials
        payload = decode_access_token(token)
        
        if payload is None:
            raise credentials_exception
        
        client_id: str = payload.get("sub")
        if client_id is None:
            raise credentials_exception
        
        client = db.query(Client).filter(Client.client_id == client_id).first()
        if client is None:
            raise credentials_exception
        
        if not client.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Client account is inactive"
            )
        
        return client
    finally:
        db.close()

