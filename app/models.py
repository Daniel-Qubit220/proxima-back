from sqlalchemy import Column, Float, BigInteger
from app.database import Base

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(BigInteger, primary_key=True, index=True)
    point_in_time = Column(BigInteger)
    interbank_rate = Column(Float)