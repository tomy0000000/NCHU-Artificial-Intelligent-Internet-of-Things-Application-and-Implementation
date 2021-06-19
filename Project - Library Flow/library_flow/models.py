from sqlalchemy import Column, ForeignKey, Integer, String
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
    title = Column(String, index=True)
    status = Column(Integer, index=True)
    floor_name = Column(String, ForeignKey("floors.name"))
    floor = relationship("Floor", back_populates="sections")

    def __repr__(self) -> str:
        return f"<Section {self.title}>"
