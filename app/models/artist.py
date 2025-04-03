from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data.database import Base


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    tracks = relationship("Track", back_populates="artist")
