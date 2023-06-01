from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from projet.models.vignette import Vignette
from config.database import get_db


class VignetteSchema(BaseModel):
    valmin: float
    valtimbre: float

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/vignette",
    tags=["vignette"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_vignette}", response_model=VignetteSchema)
def get_vignette(id_vignette: int, db: Session = Depends(get_db)):
    vignette = db.get(Vignette, id_vignette)
    if not vignette:
        raise HTTPException(status_code=404, detail="Poids vignette introuvable")
    return vignette


@router.get("/", response_model=list[VignetteSchema])
def get_all_vignette(db: Session = Depends(get_db)):
    return db.scalars(select(Vignette)).all()
