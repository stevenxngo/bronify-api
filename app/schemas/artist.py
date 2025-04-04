from pydantic import BaseModel


class ArtistBase(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        
class ArtistResponse(ArtistBase):

    class Config:
        from_attributes = True
