from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class WheatDistribution(Base):
    __tablename__ = "wheat_distributions"
    id = Column(Integer, primary_key=True, index=True)
    fps_id = Column(String)
    received = Column(String)
    issued = Column(String)
    cb = Column(String)
    yesterday_issued = Column(String)
    updated_on = Column(DateTime, default=datetime.utcnow)
