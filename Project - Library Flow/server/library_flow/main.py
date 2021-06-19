from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
@app.get("/{floor_id}", response_class=HTMLResponse)
async def floor_status(
    request: Request, floor_id: int = 1, db: Session = Depends(get_db)
):
    floors = crud.get_floors(db)
    for floor in floors:
        if floor.id == floor_id:
            floor_name = floor.name
            break
    else:
        raise HTTPException(status_code=404, detail="Floor not found")
    sections = crud.get_sections_by_floor(db, floor_id)
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "floor_name": floor_name,
            "floors": floors,
            "sections": sections,
        },
    )


@app.get("/section/{section_name}", response_model=schemas.Section)
async def read_section(section_name: str, db: Session = Depends(get_db)):
    return crud.get_section_by_name(db, section_name)


@app.post("/record", response_model=schemas.Record)
async def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    db_section = crud.get_section_by_id(db, record.section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return crud.create_record(db, record)
