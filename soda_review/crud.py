import bcrypt

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


