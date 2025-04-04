from pydantic import BaseModel


class OriginalArtistBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class OriginalArtistResponse(OriginalArtistBase):

    class Config:
        from_attributes = True
