from pydantic import BaseModel

class VehicleCreate(BaseModel):
    id: int
    brand: str
    model: str
    year: int 
    
class VehicleUpdate(BaseModel):
    brand: str
    model: str
    year: int


  