from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine
from app.database import models
from app.routes.hostel_routes import router as hostel_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(
    title="Hostel Vacancy API"
)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://hostelnest.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(hostel_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Hostel Vacancy API"
    }