from datetime import datetime
import pytz
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.data.database import Base

ET_TZ = pytz.timezone("America/New_York")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    original_title = Column(String, nullable=True)
    original_artist_id = Column(
        Integer, ForeignKey("original_artists.id"), nullable=True
    )
    filename = Column(String, unique=True, index=True)
    format = Column(String, default="mp3")
    url = Column(String, nullable=True)
    upload_date = Column(
        DateTime(timezone=True), default=lambda: datetime.now(ET_TZ)
    )

    artist = relationship("Artist")
    original_artist = relationship("OriginalArtist")

    def __repr__(self):
        return f"<Track(id={self.id}, title='{self.title}', artist_id={self.artist_id})>"
