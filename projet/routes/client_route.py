from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from projet.models.client import Client
from config.database import get_db


# app = FastAPI()
# mon_router = APIRouter()
# session = {}


class ClientSchema(BaseModel):
    codcli: int = None
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

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=ClientSchema)
def create_client(new_client: ClientSchema, db: Session = Depends(get_db)):
    with db as session:
        client = Client(**new_client.dict())
        session.add(client)
        session.commit()
        session.refresh(client)
        return client


@router.put("/update/{client_id}", response_model=ClientSchema)
def update_client(client_id, modifications: ClientSchema, db: Session = Depends(get_db)):
    with db:
        client = db.get(Client, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Ce client est introuvable")
        data = modifications.dict()
        for key, value in data.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return ClientSchema.from_orm(client)


@router.get("/{client_id}", response_model=ClientSchema)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Ce client est introuvable")
    return client


@router.get("/", response_model=list[ClientSchema])
def get_all_clients(db: Session = Depends(get_db)):
    return db.scalars(select(Client)).all()
