from pydantic import BaseModel


class OriginalArtistBase(BaseModel):
    name: str
