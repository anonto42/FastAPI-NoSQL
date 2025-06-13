from server.app.modules.user import user_service
from server.utils.send_res import send_response
from server.constants.http_status_code import HTTP_STATUS
from fastapi import Request
from .user_schema import User
from server.error.exceptions_error import APIError

async def register_user(req: Request):

    body = await req.json()
    database = req.app.database

    try:
        user = User( **body )
    except ValueError as err:
        print(err)
        raise APIError(status_code=HTTP_STATUS.Expectation_Failed, message="Invalid input data")

    result = await user_service.register_user(user,database)

    return send_response(
        True,
        "User created Successfull!",
        result,
        HTTP_STATUS.OK
    )

def get_user(req: Request):

    user = req

    result = user_service.get_profile(user)

    return send_response(
        True,
        "Get user Successfull!",
        result,
        HTTP_STATUS.OK
    )