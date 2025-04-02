from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import Optional


class TrackBase(BaseModel):
    filename: str
    title: str
    artist: Optional[str] = None
    source_url: Optional[HttpUrl] = None
    format: str = "mp3"


class TrackCreate(TrackBase):
    pass


class TrackResponse(TrackBase):
    id: int
    upload_date: datetime

    class Config:
        from_attributes = True
