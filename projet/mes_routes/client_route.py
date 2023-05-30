from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import text
from sqlalchemy import create_engine
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from projet.models.client import Client
from config.database import SessionLocal

app = FastAPI()
mon_router = APIRouter()
session = {}



class ClientSchema(BaseModel):
    genrecli: str
    nomcli: str
    prenomcli: str
    adresse1cli: str
    adresse2cli: str
    adresse3cli: str
    villecli_id: int
    telcli: str
    emailcli: str
    portcli: str
    newsletter: int


@app.post("/createclients")
async def create_client():
    with SessionLocal() as sessionclient:
        new_client = Client(
            genrecli="Monsieur",
            nomcli="Dupont",
            prenomcli="Jean",
            adresse1cli="Rue de la Paix",
            adresse2cli="",
            adresse3cli="",
            villecli_id=1,
            telcli="0123456789",
            emailcli="jean.dupont@example.com",
            portcli="",
            newsletter=1
        )
        sessionclient.add(new_client)
        sessionclient.commit()
        sessionclient.refresh(new_client)
        return new_client


@app.put("/updateclients/{client_id}")
def update_client(client_id: int):
    updated_data = {
        "genrecli": "Mr",
        "nomcli": "Jordan",
        "prenomcli": "Nike",
        "adresse1cli": "123 Rue Principale",
        "adresse2cli": "",
        "adresse3cli": "",
        "telcli": "0123456789",
        "emailcli": "nikejordany@example.com"
    }

    with SessionLocal() as sessionclient:
        client = sessionclient.query(Client).get(client_id)

        if client:
            for key, value in updated_data.items():
                setattr(client, key, value)

            sessionclient.commit()
            sessionclient.refresh(client)

            return {"message": "Client updated successfully"}

        else:
            raise HTTPException(status_code=404, detail="Client not found")

@app.get("/infoclients/{client_id}")
def get_client(client_id: int):
    with SessionLocal() as sessionclient:
        client = sessionclient.query(Client).get(client_id)

        if client:
            return client.__dict__

        else:
            raise HTTPException(status_code=404, detail="Client not found")
