from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Date, Float
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..models.commande import Commande
from ..schema.commande_schema import ClientSchema
from config.database import get_db


class CommandeSchema(BaseModel):
    codcde: int
    datcde: Date
    codcli: int
    timbrecli: Float
    timbrecde: Float
    nbcolis: int = 1
    cheqcli: Float
    idcondit: int = 0
    cdecomt: str = None
    barchive: int = 0
    bstock: int = 0


router = APIRouter(
    prefix="/commande",
    tags=["commande"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_commande}")
def get_commande(id_commande: int, db: Session = Depends(get_db())):
    commande = db.query(Commande).get(id_commande)
    if not commande:
        raise HTTPException(status_code=404, detail="Cette commande est introuvable")
    return commande

@router.get("/")
def get_all_commande(db: Session = Depends(get_db())):
    return db.query(Commande).all()


