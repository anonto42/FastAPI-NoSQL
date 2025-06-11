from .user_schema import User
from .user_model import user_model
from ....db.db_connection import db
from server.utils import crypto_context
from server.constants.http_status_code import HTTP_STATUS
from server.error.exceptions_error import APIError

async def register_user(
    payload: User
):
    existing_user = user_model.find_by_email(payload.email)
    if existing_user:
        raise APIError(status_code=HTTP_STATUS.Not_Found, message="Email is already in use")
    
    hash_password = crypto_context.hash_password(payload.password)

    try:
        new_user = user_model(
            name=payload.name,
            email=payload.email,
            hashed_password=hash_password
        )

        user = new_user.save()
        
        return dict(user)
    
    except ValueError as e :
        print(ValueError)
        raise  APIError(status_code=HTTP_STATUS.Internal_Server_Error, message=str(e))