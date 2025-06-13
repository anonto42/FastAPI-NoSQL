from .user_schema import User
from .user_model import user_model
from ....db.model import Model
from server.utils import crypto_context
from server.constants.http_status_code import HTTP_STATUS
from server.error.exceptions_error import APIError
from server.helper.otp import generate_otp
from server.helper.otp_send_on_mail import send_email

async def register_user(
    payload: User,
    db: any
):

    existing_user = db[Model.USER.value].find_one({"email": payload.email })
    if existing_user:
        raise APIError(status_code=HTTP_STATUS.Forbidden, message="Email is already in use")
    
    hash_password = crypto_context.hash_password(payload.password)

    try:
        otp = generate_otp()
    
        user_data = {
            "name": str(payload.name),
            "email": str(payload.email),
            "password": str(hash_password),
            "otp": otp
        }

        _user_ = user_model(**user_data)

        db[Model.USER.value].insert_one(_user_.dict())

        send_email(otp,payload.email,payload.name,"Verify Account")
        
        return True
    
    except ValueError as e :
        print(ValueError)
        raise  APIError(status_code=HTTP_STATUS.Internal_Server_Error, message=str(e))
    
def get_profile (
    user: any
):
    print("user profile")
    return {"Your":"lskdf"}