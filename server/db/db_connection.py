from pymongo import MongoClient
from server import env

client = MongoClient(env.MONGO_URI)

db = client[env.DATABASE_NAME]

collection = db[env.DATABASE_NAME]