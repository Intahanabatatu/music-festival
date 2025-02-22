from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Artist Pydantic Models
class ArtistBase(BaseModel):
    name: str
    genre: str
    country: str
    image_url: str

class ArtistCreate(ArtistBase):
    pass

class ArtistResponse(ArtistBase):
    id: int

    class Config:
        orm_mode = True

# Stage Pydantic Models
class StageBase(BaseModel):
    name: str
    location: str
    capacity: int

class StageCreate(StageBase):
    pass

class StageResponse(StageBase):
    id: int

    class Config:
        orm_mode = True

# Schedule Pydantic Models
class ScheduleBase(BaseModel):
    artist_id: int
    stage_id: int
    time: datetime

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleResponse(ScheduleBase):
    id: int

    class Config:
        orm_mode = True

# Ticket Pydantic Models
class TicketBase(BaseModel):
    type: str
    price: int

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int

    class Config:
        orm_mode = True

# User Pydantic Models
class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
