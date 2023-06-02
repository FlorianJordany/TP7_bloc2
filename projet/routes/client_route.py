from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from projet.models.client import Client
from config.database import get_db


# Schéma Pydantic pour la représentation des données client
class ClientSchema(BaseModel):
    codcli: int = None  # Identifiant unique du client
    genrecli: str = None  # Genre du client
    nomcli: str = None  # Nom du client
    prenomcli: str = None  # Prénom du client
    adresse1cli: str = None  # Adresse 1 du client
    adresse2cli: str = None  # Adresse 2 du client
    adresse3cli: str = None  # Adresse 3 du client
    villecli_id: int  # Identifiant de la ville du client
    telcli: str = None  # Numéro de téléphone du client
    emailcli: str = None  # Adresse e-mail du client
    portcli: str = None  # Numéro de portable du client
    newsletter: int  # Abonnement à la newsletter du client

    class Config:
        orm_mode = True

# Création d'un routeur API pour les opérations liées aux clients
router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=ClientSchema)
def create_client(new_client: ClientSchema, db: Session = Depends(get_db)):
    """
    Crée un nouveau client dans la base de données.

    Parameters:
    - **new_client**: Données du nouveau client au format JSON.

    Returns:
    - Les données du client créé au format JSON.

    Raises:
    - HTTPException 404: Si le client est introuvable.
    """
    with db as session:
        client = Client(**new_client.dict())
        session.add(client)
        session.commit()
        session.refresh(client)
        return client


@router.put("/{client_id}", response_model=ClientSchema)
def update_client(client_id, modifications: ClientSchema, db: Session = Depends(get_db)):
    """
    Met à jour un client existant dans la base de données.

    Parameters:
    - **client_id**: Identifiant du client à mettre à jour.
    - **modifications**: Données de modification du client au format JSON.

    Returns:
    - Les données du client mis à jour au format JSON.

    Raises:
    - HTTPException 404: Si le client est introuvable.
    """
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
    """
    Récupère les informations d'un client spécifique.

    Parameters:
    - **client_id**: Identifiant du client à récupérer.

    Returns:
    - Les données du client au format JSON.

    Raises:
    - HTTPException 404: Si le client est introuvable.
    """
    client = db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Ce client est introuvable")
    return ClientSchema.from_orm(client)


@router.get("/", response_model=list[ClientSchema])
def get_all_clients(db: Session = Depends(get_db)):
    """
    Récupère la liste de tous les clients.

    Returns:
    - La liste des clients au format JSON.
    """
    return db.scalars(select(Client)).all()
