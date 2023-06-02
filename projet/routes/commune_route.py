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
    commune = db.get(Commune, commune_id)
    if not commune:
        raise HTTPException(status_code=404, detail="Ce client est introuvable")
    return commune


@router.get("/", response_model=list[CommuneSchema])
def get_all_commune(db: Session = Depends(get_db)):
    return db.scalars(select(Commune)).all()


@router.post("/", response_model=CommuneSchema)
def create_commune(new_commune: CommuneSchema, db: Session = Depends(get_db)):
    with db as session:
        commune = Commune(**new_commune.dict())
        session.add(commune)
        session.commit()
        session.refresh(commune)
    return CommuneSchema.from_orm(commune)


@router.put("/{commune_id}", response_model=CommuneSchema)
def update_commune(commune_id, modifications: CommuneSchema, db: Session = Depends(get_db)):
    with db:
        commune = db.get(Commune, commune_id)
        if not commune:
            raise HTTPException(status_code=404, detail="Cette commune est introuvable")
        data = modifications.dict()
        for key, value in data.items():
            setattr(commune, key, value)
        db.commit()
        db.refresh(commune)
    return CommuneSchema.from_orm(commune)


@router.delete("/{commune_id}")
def delete_commune(commune_id: int, db: Session = Depends(get_db)):
    with db:
        commune = db.get(Commune, commune_id)
        if not commune:
            raise HTTPException(status_code=404, detail="Cette commune est introuvable")
        db.delete(commune)
        db.commit()
    return {"message": f"La commune {commune_id} à été supprimée"}
