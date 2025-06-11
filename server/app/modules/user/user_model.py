from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import uuid4

class User(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=lambda: uuid4().int, primary_key=True, index=True)
    name: str
    email: str