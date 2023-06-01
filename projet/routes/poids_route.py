from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from projet.models.poids import Poids
from config.database import get_db


class PoidsSchema(BaseModel):
    valmin: float
    valtimbre: float

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/poids",
    tags=["poids"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_poids}", response_model=PoidsSchema)
def get_poids(id_poids: int, db: Session = Depends(get_db)):
    poids = db.get(Poids, id_poids)
    if not poids:
        raise HTTPException(status_code=404, detail="Poids introuvable")
    return poids


@router.get("/", response_model=list[PoidsSchema])
def get_all_poids(db: Session = Depends(get_db)):
    return db.scalars(select(Poids)).all()
