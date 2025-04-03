from pydantic import BaseModel, HttpUrl
from typing import Optional


class TrackBase(BaseModel):
    id: int
    title: str
    artist: Optional[str] = None
    original_title: Optional[str] = None
    original_artist: Optional[str] = None
    url: Optional[HttpUrl] = None

    @classmethod
    def from_orm_with_artists(cls, track):
        data = track.__dict__.copy()
        data["artist"] = track.artist.name
        data["original_artist"] = (
            track.original_artist.name if track.original_artist else None
        )
        data.pop("artist_id", None)
        data.pop("original_artist_id", None)
        return cls.model_validate(data)
