from fastapi import APIRouter
from server.app.modules.auth.auth_route import router as auth_router
from server.app.modules.user.user_route import router as user_router

router_v1 = APIRouter()

router_v1.include_router(auth_router, prefix="/auth", tags=["auth"])
router_v1.include_router(user_router, prefix="/user", tags=["user"])