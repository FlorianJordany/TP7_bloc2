from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from projet.models.vignette import Vignette
from config.database import get_db


# Schéma Pydantic pour la représentation des données de vignette
class VignetteSchema(BaseModel):
    valmin: float  # Valeur minimale de la vignette
    valtimbre: float  # Valeur du timbre

    class Config:
        orm_mode = True

# Création d'un routeur API pour les opérations liées aux vignettes
router = APIRouter(
    prefix="/vignette",
    tags=["vignette"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_vignette}", response_model=VignetteSchema)
def get_vignette(id_vignette: int, db: Session = Depends(get_db)):
    """
    Récupère les informations d'une vignette spécifique.

    Parameters:
    - **id_vignette**: Identifiant de la vignette à récupérer.

    Returns:
    - Les données de la vignette au format JSON.

    Raises:
    - HTTPException 404: Si la vignette est introuvable.
    """
    vignette = db.get(Vignette, id_vignette)
    if not vignette:
        raise HTTPException(status_code=404, detail="Poids vignette introuvable")
    return vignette


@router.get("/", response_model=list[VignetteSchema])
def get_all_vignette(db: Session = Depends(get_db)):
    """
    Récupère la liste de toutes les vignettes.

    Returns:
    - La liste des vignettes au format JSON.
    """
    return db.scalars(select(Vignette)).all()
