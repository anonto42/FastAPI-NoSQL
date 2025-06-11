from server.app.modules.user import user_service
from server.utils.send_res import send_response
from server.constants.http_status_code import HTTP_STATUS
from fastapi import Request

async def register_user(req: Request):

    body = await req.json();

    result = await user_service.register_user(body)

    return send_response(
        True,
        "User created Successfull!",
        result,
        HTTP_STATUS.OK
    )

async def get_user(req: Request):

    print(req)

    result = await user_service.register_user()

    return send_response(
        True,
        "Get user Successfull!",
        result,
        HTTP_STATUS.OK
    )