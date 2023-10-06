from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schema.Users)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username) or crud.get_user_by_username(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    return crud.create_user(database=db, user=user)

@app.get("/users/{user_id}", response_model=schema.Users)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/sodas/", response_model=schema.Sodas)
def create_soda(soda: schema.SodaCreate, db: Session = Depends(get_db)):
    db_soda = crud.get_soda_by_name_company(db, soda_name=soda.name, soda_company=soda.company)
    if db_soda:
        raise HTTPException(status_code=400, detail="Soda already registered")
    return crud.create_soda(database=db, soda=soda)

@app.get("/sodas/{user_id}", response_model=schema.Sodas)
def read_soda(soda_id: int, db: Session = Depends(get_db)):
    db_soda = crud.get_soda(database=db, soda_id=soda_id)
    if db_soda is None:
        raise HTTPException(status_code=404, detail="Soda not found")
    return db_soda

@app.post("/reviews/", response_model=schema.Reviews)
def create_review(review: schema.ReviewCreate, db: Session = Depends(get_db)):
    db_review = crud.get_review_by_user_about_soda(database=db, user_id=review.user_id, soda_id=review.sodas_id)
    if db_review:
        raise HTTPException(status_code=400, detail="Review already done on this soda")
    return db_review