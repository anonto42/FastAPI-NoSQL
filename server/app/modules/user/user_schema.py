from pydantic import BaseModel
from typing import Optional

class user(BaseModel):
    id: Optional[str]
    name: str
    email: str
