from pydantic import BaseModel,Field
from uuid import uuid4
from typing import Optional
from enum import Enum
from datetime import datetime
from server.utils.time_stamp import current_timestamp

class UserType ( Enum ):
    USER = 'USER'
    SALES_MAN = 'SALSE_MAN'
    ADMIN = 'ADMIN'

class user_model(BaseModel):
    id: Optional[str] = str(uuid4())
    name: str
    email: str
    password: str
    isVerified: Optional[bool] = False
    otp: Optional[int]
    role: Optional[UserType] = UserType.USER.value

    # Timestamps
    created_at: datetime = Field(default_factory=current_timestamp)
    updated_at: datetime = Field(default_factory=current_timestamp)


    class Config:
        validate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote",
                "email": "tsts@gmail.com",
                "password": "alsdflakseiokllk213k",
                "role": "USER",
                "isVerified": False,
            }
        }

    class Config:
        use_enum_values = True  