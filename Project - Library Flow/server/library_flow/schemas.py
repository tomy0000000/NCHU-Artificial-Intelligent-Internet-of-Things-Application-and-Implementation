from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Section(BaseModel):
    id: int
    name: str
    status: Optional[int] = None
    guide: Optional[int] = None
    floor_name: str

    class Config:
        orm_mode = True


class Floor(BaseModel):
    id: int
    name: str
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
