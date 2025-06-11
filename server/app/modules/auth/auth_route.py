# import auth_controller
from fastapi import APIRouter,Request
from server.utils.send_res import send_response
from server.constants.http_status_code import HTTP_STATUS

router = APIRouter()

@router.post("/login")
def login(req: Request):
    # return auth_controller.login
    return