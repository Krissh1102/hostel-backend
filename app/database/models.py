from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Hostel(Base):

    __tablename__ = "hostels"
    id = Column(Integer, primary_key= True, index= True)
    hostel_name = Column(String, nullable= False)
    owner_name = Column(String, nullable = False)
    location = Column(String, nullable = False)
    contact_number = Column(String, nullable = False)
    description = Column(String, nullable = False)
    rent = Column(Integer, nullable = False)
    available_beds = Column(Integer, nullable = True)


class Student(Base):

    __tablename__= "student"
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    college=Column(String)
    phone=Column(String)
    