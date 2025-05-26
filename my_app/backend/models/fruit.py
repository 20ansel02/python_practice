from backend.core.db import Base
from sqlalchemy import Column, Integer, String, Float

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    color = Column(String)
    weight_column = Column(Float)
    price_per_kg = Column(Float)
    new_col = Column(String) 
    quantity = Column(Integer)

    def __repr__(self):
        return f"Fruit(id={self.id}, name={self.name}, color={self.color}, weight={self.weight}, price_per_kg={self.price_per_kg})"
    