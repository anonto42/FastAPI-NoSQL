import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CRYPTO_SECRETE = os.getenv("CRYPTO_SECRETE")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_HOST = os.getenv("SMTP_HOST")
HOST_IP=os.getenv("HOST_IP")
PORT=os.getenv("PORT")
MONGODB_ADMINPASSWORD= os.getenv("MONGODB_ADMINPASSWORD")
MONGODB_ADMINUSERNAME= os.getenv("MONGODB_ADMINUSERNAME")
DATABASE_NAME= os.getenv("DATABASE_NAME")