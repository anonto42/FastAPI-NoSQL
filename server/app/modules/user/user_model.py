from server.db.db_connection import db
from typing import Optional
from uuid import uuid4

class user_model:
    def __init__(self, name: str, email: str, hashed_password: str, user_id: Optional[str] = None):
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.id = user_id if user_id else str(uuid4())

    def save(self):
        # Ensure db is initialized
        if db is None:
            raise Exception("Database connection is not established.")
        
        user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.hashed_password
        }
        
        result = db.users.insert_one(user_dict)
        return result.inserted_id 

    @classmethod
    def find_by_email(cls, email: str):
        # Ensure db is initialized
        if db is None:
            raise Exception("Database connection is not established.")
            
        user_data = db.users.find_one({"email": email})
        if user_data:
            return cls(**user_data)
        return None
