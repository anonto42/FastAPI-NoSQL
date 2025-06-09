import auth_service
from fastapi import APIRouter,Request
from src.utils.send_res import send_response
from src.constants.http_status_code import HTTP_STATUS

router = APIRouter()

@router.post("/login")
async def login(req: Request):

    print(req)

    body = await req.json()

    result = await auth_service.login()

    return send_response(
        True,
        "Login Successfull!",
        result,
        HTTP_STATUS.OK
    )