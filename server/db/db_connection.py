from pymongo import MongoClient
from server.config import env
from fastapi import HTTPException
from ..error.exceptions_error import APIError
from ..constants.http_status_code import HTTP_STATUS

client = None
db = None

# Initialize database connection
def init_db():
    global client, db
    try:
        # Connect to MongoDB using the URI from the environment
        client = MongoClient(env.MONGO_URI)
        db = client[env.DATABASE_NAME]
        print("DB connected successfully: -> ", db.uri)
        
        client.server_info()  # This will send an error if the connection fails
    except Exception as e:
        raise APIError(status_code=HTTP_STATUS.Internal_Server_Error,message=f"Database connection error: {str(e)}")