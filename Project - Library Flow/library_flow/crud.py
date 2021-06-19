from sqlalchemy.orm import Session

from . import models, schemas


def get_floor(db: Session, floor_id: int):
    return db.query(models.Floor).filter(models.Floor.id == floor_id).first()


def get_floor_by_name(db: Session, name: str):
    return db.query(models.Floor).filter(models.Floor.name == name).first()


def get_floors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Floor).offset(skip).limit(limit).all()


def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Section).offset(skip).limit(limit).all()


def get_sections_by_floor(db: Session, floor_id: int):
    return db.query(models.Floor).filter(models.Floor.id == floor_id).first().sections
