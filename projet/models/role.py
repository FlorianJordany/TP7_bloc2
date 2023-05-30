from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float

from sqlalchemy.orm import relationship

from config.database import Base

class Role(Base):
    __tablename__ = "t_role"

    codrole = Column(Integer, primary_key=True)
    librole = Column(String(25), default=None)