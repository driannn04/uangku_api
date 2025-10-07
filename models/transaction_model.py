from sqlalchemy import Column, Integer, String, Numeric, Text
from config.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    amount = Column(Numeric(14, 2), nullable=False)
    type = Column(String(20), nullable=False)
    category_id = Column(Integer)
    note = Column(Text)
    date = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
