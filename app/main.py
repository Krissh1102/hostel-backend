from fastapi import FastAPI
from app.database.database import engine
from app.database import models
from app.routes.hostel_routes import router as hostel_router
from app.routes.auth_routes import router as auth_router

models.Base.metadata.create_all(bind = engine)

app = FastAPI(
    title= "Hostel Vacany API"
)
app.include_router(hostel_router)
app.include_router(auth_router)

@app.get("/")
def home():

    return{
        "message": "Welcome to the Hostel Vacancy API"
    }