from fastapi import FastAPI
from projet.routes import get_routes

app = FastAPI()
app.include_router(get_routes())
