from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    salt = Column(String)
    email = Column(String, unique=True, index=True)
    join_date = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Reviews", back_populates="owner")

class Sodas(Base):
    __tablename__ = "sodas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    company = Column(String)    

    reviews = relationship("Reviews", back_populates="soda")

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    review = Column(String)
    rating = Column(Integer)
    upvotes = Column(Integer)
    downvotes = Column(Integer)
    sodas_id = Column(Integer, ForeignKey("sodas.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="reviews")
    soda = relationship("Sodas", back_populates="reviews")

