from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from pydantic import BaseModel

from projet.models.commune import Commune
from config.database import get_db


class CommuneSchema(BaseModel):
    dep: str
    cp: str
    ville: str

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/communes",
    tags=["communes"],
    responses={404: {"description": "Not found"}})


@router.get("/{commune_id}", response_model=CommuneSchema)
def get_commune(commune_id: int, db: Session = Depends(get_db)):
    """
    **Sélectionner une commune**

    - **commune_id**: numéro d'identification de la commune.

    Retourne les données de la commune créé.
    """
    commune = db.get(Commune, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Ce client est introuvable")
    return commune


@router.get("/", response_model=list[CommuneSchema])
def get_all_commune(db: Session = Depends(get_db)):
    """
    Récupère la liste de toutes les communes.

    Returns:
    - La liste des communes au format JSON.
    """
    return db.scalars(select(Commune)).all()






