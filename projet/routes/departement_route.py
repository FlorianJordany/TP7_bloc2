from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr, conint

from ..models.departement import Departement
from config.database import get_db


class DepartementSchema(BaseModel):
    code_dept: constr(min_length=2, max_length=2)
    nom_dept: constr(min_length=2, max_length=50)
    odre_aff_dept: conint() = 0

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/departement",
    tags=["departement"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_departement}", response_model=DepartementSchema)
def get_departement(id_departement: int, db: Session = Depends(get_db)):
    departement = db.get(Departement, id_departement)
    if not departement:
        raise HTTPException(status_code=404, detail="Cette departement est introuvable")
    return departement


@router.get("/", response_model=list[DepartementSchema])
def get_all_departement(db: Session = Depends(get_db)):
    return db.scalars(select(Departement)).all()


@router.post("/", response_model=DepartementSchema)
def create_departement(new_command: DepartementSchema, db: Session = Depends(get_db)):
    with db as session:
        command = Departement(**new_command.dict())
        session.add(command)
        session.commit()
        session.refresh(command)
    return DepartementSchema.from_orm(command)


@router.put("/{departement_id}", response_model=DepartementSchema)
def update_departement(departement_id, modifications: DepartementSchema, db: Session = Depends(get_db)):
    with db:
        departement = db.get(Departement, departement_id)
        if not departement:
            raise HTTPException(status_code=404, detail="Cette departement est introuvable")
        data = modifications.dict()
        for key, value in data.items():
            setattr(departement, key, value)
        db.commit()
        db.refresh(departement)
    return DepartementSchema.from_orm(departement)


@router.delete("/{departement_id}")
def delete_departement(departement_id: int, db: Session = Depends(get_db)):
    with db as session:
        departement = db.get(Departement, departement_id)
        if not departement:
            raise HTTPException(status_code=404, detail="Cette departement est introuvable")
        db.delete(departement)
        db.commit()
    return {"message": f"La departement {departement_id} a été supprimée"}
