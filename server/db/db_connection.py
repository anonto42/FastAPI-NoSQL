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
        # Connect to MongoDB using the URI from the environment
        # mongo_uri = "mongodb://localhost:27017/"
        db_name = DATABASE_NAME
        # mongo_uri = f"mongodb://{HOST_IP}:27017"
        # mongo_uri = "mongodb://toor:root@mongo:27017"
        # mongo_uri = f"mongodb://{MONGODB_ADMINUSERNAME}:{MONGODB_ADMINPASSWORD}@mongo:27017"
        # mongo_uri = "mongodb+srv://anonto:anontom90@cluster0.1zoujuq.mongodb.net"
        
        
        client = MongoClient(MONGO_URI)
        # client = MongoClient(mongo_uri)
        
        db = client[db_name]
        
        print(Fore.MAGENTA + Back.GREEN + Style.BRIGHT + "DB connected successfully!")
        print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + "Database host is : ", Fore.GREEN + client.HOST)
        print(Fore.LIGHTBLUE_EX + Back.CYAN + Style.BRIGHT + "Database name is : ", Fore.BLUE + db_name)
        
        client.server_info()

        return  [db , client] 
    except Exception as e:
        raise APIError(status_code=HTTP_STATUS.Internal_Server_Error,message=f"Database connection error: {str(e)}")