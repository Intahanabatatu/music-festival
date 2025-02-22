from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def Home():
    return {"message": "Welcome to the Music Festival API!"}

# Artist Endpoints
@app.post("/artists/", response_model=schemas.ArtistResponse)
def add_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    return crud.create_artist(db=db, artist=artist)

@app.get("/artists/", response_model=List[schemas.ArtistResponse])
def get_artists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_artists(db=db, skip=skip, limit=limit)

# Stage Endpoints
@app.post("/stages/", response_model=schemas.StageResponse)
def add_stage(stage: schemas.StageCreate, db: Session = Depends(get_db)):
    return crud.create_stage(db=db, stage=stage)

@app.get("/stages/", response_model=List[schemas.StageResponse])
def get_stages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_stages(db=db, skip=skip, limit=limit)

# Schedule Endpoints
@app.post("/schedule/", response_model=schemas.ScheduleResponse)
def add_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db=db, schedule=schedule)

@app.get("/schedule/", response_model=List[schemas.ScheduleResponse])
def get_schedule(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_schedule(db=db, skip=skip, limit=limit)

# Ticket Endpoints
@app.post("/tickets/", response_model=schemas.TicketResponse)
def add_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db=db, ticket=ticket)

@app.get("/tickets/", response_model=List[schemas.TicketResponse])
def get_tickets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tickets(db=db, skip=skip, limit=limit)

# User Endpoints
@app.post("/users/", response_model=schemas.UserResponse)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)
