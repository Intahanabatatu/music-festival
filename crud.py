from sqlalchemy.orm import Session
from models import Artist, Stage, Schedule, Ticket, User
from schemas import ArtistCreate, StageCreate, ScheduleCreate, TicketCreate, UserCreate

# Artist CRUD
def create_artist(db: Session, artist: ArtistCreate):
    db_artist = Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Artist).offset(skip).limit(limit).all()

# Stage CRUD
def create_stage(db: Session, stage: StageCreate):
    db_stage = Stage(**stage.dict())
    db.add(db_stage)
    db.commit()
    db.refresh(db_stage)
    return db_stage

def get_stages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Stage).offset(skip).limit(limit).all()

# Schedule CRUD
def create_schedule(db: Session, schedule: ScheduleCreate):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_schedule(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Schedule).offset(skip).limit(limit).all()

# Ticket CRUD
def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ticket).offset(skip).limit(limit).all()

# User CRUD
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
