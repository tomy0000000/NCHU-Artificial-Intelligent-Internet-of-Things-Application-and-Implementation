from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
