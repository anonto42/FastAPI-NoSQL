from .user_schema import user
from .user_model import User as user_model
from ....db.db_connection import db

async def register_user(
    req: user
):
    
    return dict()