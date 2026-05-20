from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.auth_schema import StudentSignup, StudentLogin, TokenResponse
from app.services import auth_service

router = APIRouter(
    prefix= "/auth",
    tags = ["Authentication"]
)

@router.post("/signup")
def signup(user: StudentSignup, db: Session = Depends(get_db)):
    created =auth_service.signup(db, user)

    if not created:
        raise HTTPException(status_code = 400, detail = "Email Exists")
    
    return{"message": "User created successfully"}

@router.post("/login", response_model=TokenResponse)
def login(user: StudentLogin, db: Session = Depends(get_db)):
    token = auth_service.login(db, user.email, user.password),

    if not token:
        raise HTTPException(status_code= 401, details = "Invalid Credentails")
    
    return {"access_token" : token, "token_type": "bearer"}