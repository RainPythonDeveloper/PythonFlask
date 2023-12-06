# Create the database models

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

## These are models taken from Lecture 7
# Nothing new here though 

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True) # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    user_sname = Column(String(255))
    password = Column(String(255), nullable=False)

    user_cars = relationship("Car", back_populates = "owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_sname!r})"


class Car(Base):
    __tablename__ = "cars"
    car_id = Column(Integer, primary_key=True) # integer primary key will be autoincremented by default
    car_vendor = Column(String(255), nullable=False)
    car_model = Column(String(255), nullable=False)
    car_owner = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
    owner = relationship("User", back_populates="user_cars")

    def __repr__(self) -> str:
        return f"Car(car_id={self.car_id!r}, vendor={self.car_vendor!r}, model={self.car_model!r}, owner={self.car_owner!r})"
