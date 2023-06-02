from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from projet.models.poids import Poids
from config.database import get_db


# Schéma Pydantic pour la représentation des données de poids
class PoidsSchema(BaseModel):
    valmin: float  # Valeur minimale du poids
    valtimbre: float  # Valeur du timbre

    class Config:
        orm_mode = True

# Création d'un routeur API pour les opérations liées aux poids
router = APIRouter(
    prefix="/poids",
    tags=["poids"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_poids}", response_model=PoidsSchema)
def get_poids(id_poids: int, db: Session = Depends(get_db)):
    """
    Récupère les informations d'un poids spécifique.

    Parameters:
    - **id_poids**: Identifiant du poids à récupérer.

    Returns:
    - Les données du poids au format JSON.

    Raises:
    - HTTPException 404: Si le poids est introuvable.
    """
    poids = db.get(Poids, id_poids)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids introuvable")
    return poids


@router.get("/", response_model=list[PoidsSchema])
def get_all_poids(db: Session = Depends(get_db)):
    """
    Récupère la liste de tous les poids.

    Returns:
    - La liste des poids au format JSON.
    """
    return db.scalars(select(Poids)).all()
