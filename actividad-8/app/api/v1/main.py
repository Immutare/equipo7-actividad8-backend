from fastapi import FastAPI
from app.api.v1.endpoints import queries

app = FastAPI()

app.include_router(queries.router, prefix="/queries", tags=["queries"])