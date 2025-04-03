from datetime import datetime
import pytz
from sqlalchemy import Column, Integer, String, DateTime
from ..data.database import Base

ET_TZ = pytz.timezone("America/New_York")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    artist = Column(String, nullable=True)
    original_title = Column(String, nullable=True)
    original_artist = Column(String, nullable=True)
    filename = Column(String, unique=True, index=True)
    format = Column(String, default="mp3")
    url = Column(String, nullable=True)
    upload_date = Column(
        DateTime(timezone=True), default=lambda: datetime.now(ET_TZ)
    )
