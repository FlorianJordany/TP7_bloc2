import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Info de connexion a la base
DATABASE_INFO = {"driver": os.getenv('DRIVER'),
                 "username": os.getenv('DB_USERNAME'),
                 "password": os.getenv('PASSWORD'),
                 "host": os.getenv('HOST'),
                 "port": os.getenv('PORT'),
                 "database_name": os.getenv('DATABASE_NAME')
                 }

identifiants = f"{DATABASE_INFO['username']}:{DATABASE_INFO['password']}" if DATABASE_INFO["password"] != "" else DATABASE_INFO['username']

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = f"{DATABASE_INFO['driver']}://{identifiants}@{DATABASE_INFO['host']}:{DATABASE_INFO['port']}/{DATABASE_INFO['database_name']}"

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(bind=engine)


def initialize_database():
    Base.metadata.create_all(engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()