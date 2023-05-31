from sqlalchemy import Column, Integer, String, ForeignKey, Index

from config.database import Base

class Enseigne(Base):
    __tablename__ = "t_enseigne"

    id_enseigne = Column(Integer, primary_key=True)
    lb_enseigne = Column(String(50), default=None)
    ville_enseigne = Column(String(50), default=None)
    dept_enseigne = Column(Integer, default=0)
