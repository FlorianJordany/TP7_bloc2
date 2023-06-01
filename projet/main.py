from fastapi import FastAPI
from projet.routes import get_routes
from config.database import initialize_database

app = FastAPI()
app.include_router(get_routes())

if __name__ == "__main__":
    initialize_database()
