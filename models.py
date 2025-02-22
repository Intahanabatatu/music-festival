from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

# Artist Model
class Artist(Base):
    __tablename__ = 'artists'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(String)
    country = Column(String)
    image_url = Column(String)
    stage_id = Column(Integer, ForeignKey('stages.id'))

    stage = relationship("Stage", back_populates="artists")

# Stage Model
class Stage(Base):
    __tablename__ = 'stages'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity = Column(Integer)

    artists = relationship("Artist", back_populates="stage")
    schedules = relationship("Schedule", back_populates="stage")

# Schedule Model
class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    stage_id = Column(Integer, ForeignKey('stages.id'))
    time = Column(DateTime)

    artist = relationship("Artist")
    stage = relationship("Stage")

# Ticket Model
class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # E.g., "VIP", "Day Pass"
    price = Column(Integer)

# User Model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # "admin", "artist", "attendee"
