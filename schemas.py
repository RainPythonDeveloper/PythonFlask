# Create the Pydantic models
# To avoid confusion between the SQLAlchemy models and the Pydantic models, 
# we will have the file models.py with the SQLAlchemy models, and the file schemas.py 
# with the Pydantic models.

# These Pydantic models define more or less a "schema" (a valid data shape).

# pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
# Define how data should be in pure, canonical Python; validate it with pydantic.

from pydantic import BaseModel

# Create an CarBase and UserBase Pydantic models or just schemas 
# to have common attributes while creating or reading data.

class CarBase(BaseModel):
    car_vendor: str
    car_model: str

    
class CarCreate(CarBase):
    pass

# will be used when reading data, when returning it from the API.
# Config class: Behaviour of pydantic can be controlled via the Config class on a model or a pydantic dataclass
# orm_mode: will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
class Car(CarBase):
    car_id: int
    car_owner: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    login: str
    user_fname: str
    user_sname: str

class UserCreate(UserBase):
    password: str

# will be used when reading data, when returning it from the API.
class User(UserBase):
    user_id: int
    user_cars: list[Car] = []

    class Config:
        orm_mode = True
