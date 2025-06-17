from server.app.modules.auth import auth_service
from fastapi import APIRouter,Request
from ....constants.http_status_code import HTTP_STATUS
from ....utils.send_res import send_response

async def login(req):

    body = req.json()

    result = auth_service.login(body)

    return send_response(
        True,
        "Login Successfull!",
        result,
        HTTP_STATUS.OK
    )