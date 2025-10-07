from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    goal_name = Column(String(255), nullable=False)
    target_amount = Column(Float, nullable=False)
    current_amount = Column(Float)
    deadline = Column(String)
    status = Column(String(20))
    created_at = Column(String)
