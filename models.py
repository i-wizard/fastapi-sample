from sqlalchemy import String, Boolean, Integer, Float, Column,Text

from database import BaseClass

class Item(BaseClass):
    __tablename__ = 'items'
    id=Column(Integer, primary_key=True)
    name=Column(String(255), unique=True, nullable=False)
    description=Column(Text)
    on_offer=Column(Boolean, default=False)
    price=Column(Float)
    
    def __repr__(self):
        return f"{self.name}-{self.price}"