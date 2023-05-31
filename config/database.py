import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Info de connexion a la base
DATABASE_INFO = {"driver": "mysql+pymysql",
                 "username": "root",
                 "password": "root",
                 "host": "localhost",
                 "port": os.getenv('DATABASE_PORT'),
                 "database_name": "fromagerie_com"
                 }

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = f"{DATABASE_INFO['driver']}://{DATABASE_INFO['username']}:{DATABASE_INFO['password']}@{DATABASE_INFO['host']}:{DATABASE_INFO['port']}/{DATABASE_INFO['database_name']}"

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(bind=engine)


def initialize_database():
    Base.metadata.create_all(engine)

<<<<<<< HEAD

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    initialize_database()
=======

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    initialize_database()
>>>>>>> main
