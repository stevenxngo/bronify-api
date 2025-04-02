from datetime import datetime
import pytz
from sqlalchemy import Column, Integer, String, DateTime
from ..data.database import Base

BOSTON_TZ = pytz.timezone("America/New_York")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=True)
    source_url = Column(String, nullable=True)
    format = Column(String, default="mp3")
    upload_date = Column(
        DateTime(timezone=True), default=lambda: datetime.now(BOSTON_TZ)
    )
