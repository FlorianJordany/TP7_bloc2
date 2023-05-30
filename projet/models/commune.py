from sqlalchemy import Column, Integer, String, ForeignKey, Index

from config.database import Base


class Commune(Base):
    __tablename__ = "t_communes"

    id = Column(Integer, primary_key=True)
    dep = Column(String(2), ForeignKey('t_dept.code_dept'))
    cp = Column(String(5), default=None)
    ville = Column(String(50), default=None)

    __table_args__ = (Index('commune_index', "dep", "cp", "ville"),)
