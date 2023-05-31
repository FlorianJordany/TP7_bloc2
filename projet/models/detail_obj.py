from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float

from sqlalchemy.orm import relationship

from config.database import Base

class DetailObjet(Base):
    __tablename__ = "t_dtlcode_codobj"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('t_dtlcode.id'))
    objet_id = Column(Integer, ForeignKey('t_objet.codobj'))