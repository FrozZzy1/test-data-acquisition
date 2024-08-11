from fastapi import APIRouter, FastAPI

from app.api.handlers.users import users_router
from app.api.handlers.items import items_router

app = FastAPI(
    title='admin panel',
)

router = APIRouter(
    prefix='/api/v1/adminpanel',
)

router.include_router(users_router)
router.include_router(items_router)
app.include_router(router)
