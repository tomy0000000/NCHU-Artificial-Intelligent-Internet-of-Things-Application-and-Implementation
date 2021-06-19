from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_floors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Floor).offset(skip).limit(limit).all()


def get_section_by_id(db: Session, section_id):
    return db.query(models.Section).filter(models.Section.id == section_id).first()


def get_section_by_name(db: Session, section_name: str):
    return db.query(models.Section).filter(models.Section.name == section_name).first()


def get_sections_by_floor(db: Session, floor_id: int):
    return db.query(models.Floor).filter(models.Floor.id == floor_id).first().sections


def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
