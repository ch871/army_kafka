from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

engine = create_engine(os.environ['PSQL_DB_URL'])
session_maker = sessionmaker(bind=engine)


def get_mongo_client():
    return MongoClient(os.environ['MONGO_URL'])


def get_messages_collection():
    db = get_mongo_client()['army']
    return db['messages']
