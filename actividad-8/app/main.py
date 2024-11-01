from fastapi import FastAPI

from app.core.events import create_start_app_handler
from app.core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.api.routes.api import router as api_router



def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()
