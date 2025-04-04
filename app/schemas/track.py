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
    def from_orm(cls, obj):
        data = obj.__dict__.copy()
        data["artist"] = obj.artist.name
        data["original_artist"] = (
            obj.original_artist.name if obj.original_artist else None
        )
        data.pop("artist_id", None)
        data.pop("original_artist_id", None)
        return cls.model_validate(data)

    class Config:
        from_attributes = True


class TrackResponse(TrackBase):
    play_url: Optional[str] = None

    @classmethod
    def from_orm(cls, obj):
        base_data = super().from_orm(obj).dict()
        base_data["play_url"] = f"/track/play/{obj.id}"
        return cls.model_validate(base_data)

    class Config:
        from_attributes = True
