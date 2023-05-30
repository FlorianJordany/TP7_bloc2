from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float

from sqlalchemy.orm import relationship

from config.database import Base

class Poids(Base):
    __tablename__ = "t_poids"

    id = Column(Integer, primary_key=True)
    valmin = Column(Numeric, default=0)
    valtimbre = Column(Numeric, default=0)