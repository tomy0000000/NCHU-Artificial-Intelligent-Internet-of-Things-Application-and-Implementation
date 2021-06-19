from typing import List, Optional
from pydantic import BaseModel


class SectionBase(BaseModel):
    title: str
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
