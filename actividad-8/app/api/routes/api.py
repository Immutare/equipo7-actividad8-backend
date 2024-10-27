from fastapi import APIRouter

from app.api.routes import predictor
from app.api.routes.queries import queries_controller

router = APIRouter()

router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(queries_controller.router, tags=["queries"], prefix="/queries")
