from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..models.conditionnement import Conditionnement
from config.database import get_db


class ConditionnementSchema(BaseModel):
    idcondit : int = None
    libcondit: str
    poidscondit: int
    prixcond: float
    ordreimp: int

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/conditionnement",
    tags=["conditionnement"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{poids_commande_gramme}", response_model=ConditionnementSchema)
def get_conditionnement_by_weight(poids_commande_gramme: int, db: Session = Depends(get_db)):
    conditionnement = db.query(Conditionnement).filter(
        Conditionnement.poidscondit >= poids_commande_gramme
    ).order_by(
        Conditionnement.poidscondit
    ).first()

    if not conditionnement:
        raise HTTPException(status_code=404, detail="Aucun conditionnement disponible pour ce poids")

    return conditionnement


@router.get("/", response_model=list[ConditionnementSchema])
def get_all_conditionnement(db: Session = Depends(get_db)):
    return db.scalars(select(Conditionnement)).all()


@router.post("/", response_model=ConditionnementSchema)
def create_conditionnement(new_conditionnement: ConditionnementSchema, db: Session = Depends(get_db)):
    with db as session:
        conditionnement = Conditionnement(**new_conditionnement.dict())
        session.add(conditionnement)
        session.commit()
        session.refresh(conditionnement)
    return ConditionnementSchema.from_orm(conditionnement)


@router.delete("/{idcondit}")
def delete_conditionnement(idcondit: int, db: Session = Depends(get_db)):
    with db:
        conditionnement = db.get(Conditionnement, idcondit)
        if not conditionnement:
            raise HTTPException(status_code=404, detail="Le conditionnement est introuvable")
        db.delete(conditionnement)
        db.commit()
    return {"message": f"Le conditionnement {idcondit} a été supprimé"}