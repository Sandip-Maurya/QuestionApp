from config import (
    MONGODB_CONNECTION_URL, 
    JEE_DB_Name, 
    NEET_DB_Name, 
    QUESTIONS_COLLECTION_NAME,
    ADMIN_DB_Name,
    CHAPTER_COLLECTION_NAME,
    TOPIC_COLLECTION_NAME
)
from pymongo import MongoClient

client = MongoClient(MONGODB_CONNECTION_URL)

# To get the questions
jee_db = client[JEE_DB_Name]
neet_db = client[NEET_DB_Name]
jee_collection = jee_db[QUESTIONS_COLLECTION_NAME]
neet_collection = neet_db[QUESTIONS_COLLECTION_NAME]

# To get the chapters and topics
admin_db = client[ADMIN_DB_Name]
chapter_collection = admin_db[CHAPTER_COLLECTION_NAME]
topic_collection = admin_db[TOPIC_COLLECTION_NAME]
