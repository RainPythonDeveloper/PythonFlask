# CReateUpdateDelete utils (CRUD)
# reusable functions to interact with the data in the database.

from sqlalchemy.orm import Session
import models, schemas

# getting a user by login from a query to Users table using SQLAlchemy model User
def get_user_by_login(db: Session, user_login: int)->Session.query:
    return db.query(models.User).filter(models.User.login == user_login).first()

# getting a user by fname from a query to Users table using SQLAlchemy model User
# returns a list of user objects as a query
def get_user_by_fname(db: Session, user_fname: str)->Session.query:
    return db.query(models.User).filter(models.User.user_fname == user_fname).all()

# getting all users from a query to Users table using SQLAlchemy model User
def get_all_users(db: Session, skip: int = 0, limit: int = 100)->Session.query:
    return db.query(models.User).offset(skip).limit(limit).all()

# getting a car by a car_id field 
def get_car_by_id(db: Session, car_id: int)->Session.query:
    return db.query(models.Car).filter(models.Car.car_id == car_id).first()

# getting a user cars
def get_user_cars(db: Session, user_id: int)->Session.query:
    return db.query(models.Car).filter(models.Car.car_owner == user_id).all()

# getting all cars
def get_all_cars(db: Session, skip: int = 0, limit: int = 100)->Session.query:
    return db.query(models.Car).offset(skip).limit(limit).all()

# creating a user from instance of UserCreate
def create_user(db: Session, user: schemas.UserCreate)->models.User:
    new_user = models.User(login=user.login, 
                            user_fname=user.user_fname,
                            user_sname=user.user_sname,
                            password=user.password)
    # new_user = models.User(**user.dict()) # this is actually the same as above
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(user_id: int, db: Session)->None:
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    # new_user = models.User(**user.dict()) # this is actually the same as above
    db.delete(user)
    db.commit()
    

# creating a car from instance of CarCreate
def create_car(db: Session, car: schemas.CarCreate, user_id)->models.Car:
    # new_car = models.Car(car_vendor=car.car_vendor,
    #                         car_model=car.car_model,
    #                         car_owner=user_id)
    
    new_car = models.Car(**car.dict(), car_owner=user_id)
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car



