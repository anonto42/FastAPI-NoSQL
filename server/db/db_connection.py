from pymongo import MongoClient
from server.config import env

client = MongoClient(env.MONGO_URI)

db = client[env.DATABASE_NAME]