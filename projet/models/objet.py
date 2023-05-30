from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float

from sqlalchemy.orm import relationship

from config.database import Base


class Objet(Base):
    __tablename__ = "t_objet"

    codobj = Column(Integer, primary_key=True)
    libobj = Column(String(50), default=None)
    tailleobj = Column(String(50), default=None)
    puobj = Column(Numeric, default=0.0000)
    poidsobj = Column(Numeric, default=0.0000)
    indispobj = Column(Integer, default=0)
    o_imp = Column(Integer, default=0)
    o_aff = Column(Integer, default=0)
    o_cartp = Column(Integer, default=0)
    points = Column(Integer, default=0)
    o_ordre_aff = Column(Integer, default=0)
    condit = relationship("ObjetCond", back_populates='objets')
