from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import router
from src.database.models import create_database_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "http://telegram_bot",
    "http://backend",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"], 
)

app.include_router(router=router)
