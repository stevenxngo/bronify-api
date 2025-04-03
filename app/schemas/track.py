from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import Optional


class TrackBase(BaseModel):
    title: str
    artist: Optional[str] = None
    original_title: Optional[str] = None
    original_artist: Optional[str] = None
    url: Optional[HttpUrl] = None


class TrackResponse(TrackBase):
    id: int
    upload_date: datetime

    class Config:
        from_attributes = True
