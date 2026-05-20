from sqlalchemy.orm import Session
from app.database import models 
from app.schemas.hostel_schema import HostelCreate


def create_hostel(db: Session, hostel: HostelCreate):
    new_hostel = models.Hostel(**hostel.model_dump())

    db.add(new_hostel)
    db.commit()
    db.refresh(new_hostel)
    return new_hostel

def get_all_hostels(db: Session):
    return db.query(models.Hostel).all()

def get_single_hostel(db: Session, hostel_id: int):
    return db.query(models.Hostel).filter(
        models.Hostel.id == hostel_id
    ).first()

def update_hostel(db: Session, hostel_id:int, hostel_data: HostelCreate):
    
    hostel = db.query(models.Hostel).filter(
        models.Hostel.id == hostel_id
    ).first()

    if not hostel:
        return None
    
    hostel.hostel_name = hostel_data.hostel_name
    hostel.owner_name = hostel_data.owner_name
    hostel.location = hostel_data.location
    hostel.rent = hostel_data.rent
    hostel.available_beds = hostel_data.available_beds
    hostel.contact_number = hostel_data.contact_number
    hostel.description = hostel_data.description
    
    db.commit()
    db.refresh(hostel)
    return hostel


def delete_hostel(db: Session, hostel_id: int):

    hostel = db.query(models.Hostel).filter(
        models.Hostel.id == hostel_id
    ).first()

    if not hostel:
        return None

    db.delete(hostel)
    db.commit()
    return hostel




