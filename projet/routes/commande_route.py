from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..models.commande import Commande
from config.database import get_db


class CommandeSchema(BaseModel):
    codcde: int
    datcde: date
    codcli: int
    timbrecli: float
    timbrecde: float
    nbcolis: int = 1
    cheqcli: float
    idcondit: int = 0
    cdeComt: str = None
    barchive: int = 0
    bstock: int = 0

    class Config:
        orm_mode = True


router = APIRouter(
    prefix="/commande",
    tags=["commande"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_commande}", response_model=CommandeSchema)
def get_commande(id_commande: int, db: Session = Depends(get_db)):
    commande = db.get(Commande, id_commande)
    if not commande:
        raise HTTPException(status_code=404, detail="Cette commande est introuvable")
    return commande


@router.get("/", response_model=list[CommandeSchema])
def get_all_commande(db: Session = Depends(get_db)):
    return db.scalars(select(Commande)).all()


@router.get("/points/{id_commande}")
def get_points(id_commande: int, db: Session = Depends(get_db)):
    sql_statement = f"""SELECT SUM(t_dtlcode.qte*t_objet.points) as points FROM t_dtlcode_codobj
                    INNER JOIN t_objet ON objet_id = codobj
                    INNER JOIN t_dtlcode ON detail_id = t_dtlcode.id
                    WHERE detail_id IN (SELECT id FROM t_dtlcode WHERE codcde = {id_commande});"""
    points = db.execute(text(sql_statement))
    result = points.fetchone().points
    return result


@router.post("/", response_model=CommandeSchema)
def create_commande(new_command: CommandeSchema, db: Session = Depends(get_db)):
    with db as session:
        command = Commande(**new_command.dict())
        session.add(command)
        session.commit()
        session.refresh(command)
    return CommandeSchema.from_orm(command)


@router.put("/{command_id}", response_model=CommandeSchema)
def update_commande(commande_id, modifications: CommandeSchema, db: Session = Depends(get_db)):
    with db:
        commande = db.get(Commande, commande_id)
        if not commande:
            raise HTTPException(status_code=404, detail="Cette commande est introuvable")
        data = modifications.dict()
        for key, value in data.items():
            setattr(commande, key, value)
        db.commit()
        db.refresh(commande)
    return CommandeSchema.from_orm(commande)


@router.delete("/{commande_id}", include_in_schema=False)
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    with db:
        commande = db.get(Commande, commande_id)
        if not commande:
            raise HTTPException(status_code=404, detail="Cette commande est introuvable")
        db.delete(commande)
        db.commit()
    return {"message": f"La commande {commande_id} a été supprimée"}


@router.get("/count")
def get_command_count(db: Session = Depends(get_db)):
    return db.scalars()
