from fastapi import FastAPI
from app.routes.git_routes import router

app = FastAPI(title="GitHub Cloud Connector")

app.include_router(router)