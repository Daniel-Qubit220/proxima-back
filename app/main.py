from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import SessionLocal, engine
from app import models
from dotenv import load_dotenv
from typing import List


load_dotenv()

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class ExchangeRateInput(BaseModel):
    point_in_time: int
    interbank_rate: float


class ExchangeRateOutput(BaseModel):
    point_in_time: int
    interbank_rate: float


@app.post("/exchange-rate/", response_model=List[ExchangeRateOutput])
def create_exchange_rates(rates: List[ExchangeRateInput]):
    db = SessionLocal()
    db_rates = []
    for rate in rates:
        db_rate = models.ExchangeRate(**rate.model_dump())
        db.add(db_rate)
        db_rates.append(db_rate)
    db.commit()
    db.close()
    return db_rates


@app.get("/exchange-rate/{point_in_time}", response_model=ExchangeRateOutput)
def get_exchange_rate(point_in_time: int):
    db = SessionLocal()
    exchange_rate = db.query(models.ExchangeRate).filter(models.ExchangeRate.point_in_time == point_in_time).first()
    db.close()
    if exchange_rate is None:
        raise HTTPException(status_code=404, detail="Exchange rate not found")
    return exchange_rate


@app.get("/exchange-rates/", response_model=List[ExchangeRateOutput], tags=["Exchange Rates"])
def get_all_exchange_rates():
    """
       Get all exchange rates.

       Returns a list of all stored exchange rates.
    """
    db = SessionLocal()
    all_rates = db.query(models.ExchangeRate).all()
    db.close()
    return all_rates