from sqlalchemy import Column, Integer, String
from config.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    icon = Column(String(100))
    color = Column(String(7))
    created_at = Column(String)
