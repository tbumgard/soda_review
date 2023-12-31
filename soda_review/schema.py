from pydantic import BaseModel

class ReviewBase(BaseModel):
    sodas_id: int
    user_id: int

class ReviewCreate(ReviewBase):
    review: str
    rating: int

class Reviews(ReviewBase):
    id: int
    review: str
    rating: int
    upvotes: int
    downvotes: int
        
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    email: str
    first_name: str
    last_name: str

class UserVerify(UserBase):
#    password: str
    pass    

class Users(UserBase):
    id: int
    password: str
    salt: str
    email: str
    join_date: str
    first_name: str
    last_name: str
    reviews: list[Reviews] = []

    class Config:
        orm_mode = True


class SodaBase(BaseModel):
    name: str
    company: str       

class SodaCreate(SodaBase):
    pass

class Sodas(SodaBase):
    id: int
    reviews: list[Reviews] = []

    class Config:
        orm_mode = True

