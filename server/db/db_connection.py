from pymongo import MongoClient
from ..config.env import DATABASE_NAME, MONGODB_ADMINPASSWORD, MONGODB_ADMINUSERNAME, MONGO_URI, HOST_IP
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
        
        db_name = DATABASE_NAME
        
        client = MongoClient(MONGO_URI)
        
        db = client[db_name]
        
        print(Fore.MAGENTA + Back.GREEN + Style.BRIGHT + "DB connected successfully!")
        print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + "Database host is : ", Fore.GREEN + client.HOST)
        print(Fore.LIGHTBLUE_EX + Back.CYAN + Style.BRIGHT + "Database name is : ", Fore.BLUE + db_name)
        
        client.server_info()

        return  client 
    
    except Exception as e:
        raise APIError(status_code=HTTP_STATUS.Internal_Server_Error,message=f"Database connection error: {str(e)}")