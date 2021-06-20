from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SectionBase(BaseModel):
    name: str
    status: Optional[int] = None


class SectionUpdate(SectionBase):
    pass


class Section(SectionBase):
    id: int
    floor_name: str

    class Config:
        orm_mode = True


class FloorBase(BaseModel):
    name: str


class Floor(FloorBase):
    id: int
    sections: List[Section] = []

    class Config:
        orm_mode = True


class Record(BaseModel):
    id: int
    status: int
    timestamp: datetime
    section_id: int

    class Config:
        orm_mode = True


class RecordCreate(BaseModel):
    section_id: int
    device_list: Optional[List[str]] = None
    status: Optional[int] = None
