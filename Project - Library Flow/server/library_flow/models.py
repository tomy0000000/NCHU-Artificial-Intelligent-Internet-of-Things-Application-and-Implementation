from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Floor(Base):
    __tablename__ = "floors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    sections = relationship("Section", back_populates="floor")

    def __repr__(self) -> str:
        return f"<Floor {self.name}>"


class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Integer, index=True)
    floor_name = Column(String, ForeignKey("floors.name"))
    floor = relationship("Floor", back_populates="sections")
    records = relationship("Record", back_populates="section")

    def __repr__(self) -> str:
        return f"<Section {self.title}>"


class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    section_id = Column(Integer, ForeignKey("sections.id"))
    section = relationship("Section", back_populates="records")

    def __repr__(self) -> str:
        return f"<Record of {self.section_id} at {self.timestamp}>"
