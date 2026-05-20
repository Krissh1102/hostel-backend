from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.hostel_schema import(HostelCreate, HostelResponse)
from app.services import hostel_service

router = APIRouter(
    prefix = "/hostels",
    tags = ["Hostels"]
)

@router.post("/",response_model= HostelResponse)
def create_hostel(hostel: HostelCreate, db: Session = Depends(get_db)):
    return hostel_service.create_hostel(db, hostel)


@router.get("/", response_model=list[HostelResponse])
def get_all_hostels(
    db: Session = Depends(get_db)
):
    return hostel_service.get_all_hostels(db)

@router.get("/{hostel_id}",  response_model=HostelResponse)
def get_single_hostel(
    hostel_id: int, 
    db : Session = Depends(get_db)
):
    hostel = hostel_service.get_single_hostel(db, hostel_id)

    if not hostel:
        raise HTTPException(status_code= 404, detail="Hostel not found")
    
    return hostel


@router.put("/{hostel_id}", response_model=HostelResponse)
def update_hostel(
    hostel_id: int,
    hostel: HostelCreate,
    db: Session = Depends(get_db)
):

    updated_hostel = hostel_service.update_hostel(
        db,
        hostel_id,
        hostel
    )

    if not updated_hostel:
        raise HTTPException(
            status_code=404,
            detail="Hostel not found"
        )
    return updated_hostel


@router.delete("/{hostel_id}")
def delete_hostel(
    hostel_id: int,
    db: Session = Depends(get_db)
):
    deleted_hostel = hostel_service.delete_hostel(
        db,
        hostel_id
    )
    if not deleted_hostel:
        raise HTTPException(
            status_code=404,
            detail="Hostel not found"
        )
    return {
        "message": "Hostel deleted successfully"
    }