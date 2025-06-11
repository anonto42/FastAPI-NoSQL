from server.app.modules.user.user_schema import user
from server.app.modules.user.user_model import User as user_model
from server.helper import crud

async def register_user(
    req: user
):
    new_user = crud.create_item(user_model,req)
    
    return dict(new_user)