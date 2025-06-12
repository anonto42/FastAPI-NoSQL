from pymongo import MongoClient
from server.config import env
from fastapi import HTTPException
from ..error.exceptions_error import APIError
from ..constants.http_status_code import HTTP_STATUS
from colorama import init, Fore, Back, Style

init(autoreset=True)

client = None
db = None

# Initialize database connection
def init_db():
    global client, db
    try:
        # Connect to MongoDB using the URI from the environment
        client = MongoClient(env.MONGO_URI)
        db = client[env.DATABASE_NAME]
        print(Fore.MAGENTA + Back.GREEN + Style.BRIGHT + "DB connected successfully!")
        print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + "Database host is : ", Fore.GREEN + env.MONGO_URI)
        print(Fore.LIGHTBLUE_EX + Back.CYAN + Style.BRIGHT + "Database name is : ", Fore.BLUE + env.DATABASE_NAME)
        
        client.server_info()  # This will send an error if the connection fails

        return  [db , client] 
    except Exception as e:
        raise APIError(status_code=HTTP_STATUS.Internal_Server_Error,message=f"Database connection error: {str(e)}")