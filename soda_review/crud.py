import bcrypt
import time

from sqlalchemy.orm import Session

from . import models, schema

def get_user(database: Session, user_id: int):
    return database.query(models.Users).filter(models.Users.id == user_id).first()

def get_user_by_username(database: Session, username: str):
    return database.query(models.Users).filter(models.Users.username == username).first()

def get_user_by_email(database: Session, email: str):
    return database.query(models.Users).filter(models.Users.email == email).first()

def get_soda(database: Session, soda_id: int):
    return database.query(models.Sodas).filter(models.Sodas.id == soda_id).first()

def get_soda_by_name_company(database: Session, soda_name: str, soda_company: str):
    return database.query(models.Sodas).filter(models.Sodas.name == soda_name, models.Sodas.company == soda_company).first()

def get_review_by_user_about_soda(database: Session, user_id: int, soda_id: int):
    return database.query(models.Reviews).filter(models.Reviews.user_id == user_id, models.Reviews.sodas_id == soda_id).first()

def get_reviews_by_user(database: Session, user_id: int):
    return database.query(models.Reviews).filter(models.Reviews.user_id == user_id).all()

def get_reviews_by_soda(database: Session, soda_id: int):
    return database.query(models.Reviews).filter(models.Reviews.sodas_id == soda_id).all()

def create_user(database: Session, user: schema.UserCreate):
    
    # Encrypt password with a salt
    bytes = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    db_user = models.Users(username=user.username, password=hash, salt=salt, email=user.email, join_date=time.asctime(), 
                           first_name=user.first_name, last_name=user.last_name)
   
    database.add(db_user)
    database.commit()
    database.refresh(db_user)
    return db_user
    
def create_soda(database: Session, soda: schema.SodaCreate):
    db_soda = models.Sodas(name=soda.name, company=soda.company)

    database.add(db_soda)
    database.commit()
    database.refresh(db_soda)
    return db_soda

def create_review(database: Session, review: schema.ReviewCreate):
    db_review = models.Reviews(sodas_id=review.sodas_id, user_id=review.user_id, review=review.review, rating=review.rating, 
                               upvotes=0, downvotes=0)
    database.add(db_review)
    database.commit()
    database.refresh(db_review)
    return db_review

def user_verify(database: Session, user: schema.UserVerify):
    return database.query(models.Users).filter(models.Users.id == user.username).first()

    
