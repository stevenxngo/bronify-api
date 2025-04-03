from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data.database import Base


class OriginalArtist(Base):
    __tablename__ = "original_artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    tracks = relationship("Track", back_populates="original_artist")
