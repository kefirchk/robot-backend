from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import routers
from src.configs.api_config import APIConfig

app = FastAPI(title="Robot API")
api_config = APIConfig()

for router in routers:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=api_config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
