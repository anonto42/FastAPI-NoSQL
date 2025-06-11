import auth_service
from fastapi import APIRouter,Request

async def login(req):
    print(req)

    body = await req.json()

    result = await auth_service.login()

    return send_response(
        True,
        "Login Successfull!",
        result,
        HTTP_STATUS.OK
    )