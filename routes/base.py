from fastapi import FastAPI , APIRouter
import os

base_router = APIRouter(
    prefix="/Mina"
)


@base_router.get("/")
async def welcome():
    appname = os.getenv("APP_NAME")
    return  {
        "message" : "how are you",
        "app name" : appname
    }

