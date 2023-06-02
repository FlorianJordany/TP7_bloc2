from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr, conint

from ..models.departement import Departement
from config.database import get_db


class DepartementSchema(BaseModel):
    code_dept: constr(min_length=2, max_length=2)
    nom_dept: constr(min_length=2, max_length=50)
    ordre_aff_dept: conint() = 0

    class Config:
        def __init__(self):
            pass

        orm_mode = True


router = APIRouter(
    prefix="/departement",
    tags=["departement"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_departement}", response_model=DepartementSchema)
def get_departement(id_departement: int, db: Session = Depends(get_db)):
    """
    **Sélectionner un département**

    - **id_departement**: numéro d'identification du département.

    Retourne les données du département créé.
    """
    departement = db.get(Departement, id_departement)
    if not departement:
        raise HTTPException(status_code=404, detail="Cette departement est introuvable")
    return departement


@router.get("/", response_model=list[DepartementSchema])
def get_all_departement(db: Session = Depends(get_db)):
    """
    Récupère la liste de tous les départements.

    Returns:
    - La liste des départements au format JSON.
    """
    return db.scalars(select(Departement)).all()

