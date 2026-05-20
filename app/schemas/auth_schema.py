from pydantic import BaseModel, EmailStr


class StudentSignup(BaseModel):

    full_name: str
    email: str
    password: str
    college: str
    phone: str


class StudentLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str