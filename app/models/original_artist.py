from sqlalchemy import Column, Integer, String
from app.data.database import Base


class OriginalArtist(Base):
    __tablename__ = "original_artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
