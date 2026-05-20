from pydantic import BaseModel
from typing import Optional

class HostelBase(BaseModel):

    hostel_name: str
    owner_name : str
    location: str
    contact_number: str
    description: Optional[str] =  None
    rent : int
    available_beds: int

class HostelCreate(HostelBase):
    pass

class HostelResponse(HostelBase):
    id: int 
    class Config:
        from_attribute = True