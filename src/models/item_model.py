from sqlalchemy import Column, Integer, String
from src.db import Base

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)