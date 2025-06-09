from fastapi import APIRouter
from src.app.modules.auth.auth_route import router as auth_router

router_v1 = APIRouter()

router_v1.include_router(auth_router, prefix="/auth", tags=["auth"])