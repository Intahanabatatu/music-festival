from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Mock Database (in-memory data storage)
artists_db = {}
ratings_db = {}
stages_db = {}
schedule_db = {}
tickets_db = {}
users_db = {}

# Pydantic Models

# Artist Model
class Artist(BaseModel):
    name: str
    genre: str
    country: str
    image: str

# Rating Model
class Rating(BaseModel):
    user_id: int
    rating: int
    comment: str

# Stage Model
class Stage(BaseModel):
    name: str
    location: str
    capacity: int

# Schedule Model
class Schedule(BaseModel):
    artist_id: str
    stage_id: str
    day: str
    time: str

# Ticket Model
class Ticket(BaseModel):
    type: str
    price: float

# User Model
class User(BaseModel):
    username: str
    email: str
    password: str

# Artist Management Endpoints
@app.get("/artists/", tags=["Artist Management"])
def get_artists():
    return list(artists_db.values())

@app.get("/artists/{id}", tags=["Artist Management"])
def get_artist(id: str):
    if id not in artists_db:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artists_db[id]

@app.post("/artists/", tags=["Artist Management"])
def add_artist(artist: Artist):
    artist_id = str(uuid4())
    artists_db[artist_id] = artist
    return {"id": artist_id, "artist": artist}

@app.put("/artists/{id}", tags=["Artist Management"])
def update_artist(id: str, artist: Artist):
    if id not in artists_db:
        raise HTTPException(status_code=404, detail="Artist not found")
    artists_db[id] = artist
    return {"id": id, "artist": artist}

@app.delete("/artists/{id}", tags=["Artist Management"])
def delete_artist(id: str):
    if id not in artists_db:
        raise HTTPException(status_code=404, detail="Artist not found")
    del artists_db[id]
    return {"message": "Artist deleted"}

# Rating Endpoints
@app.post("/rating/artists/{artist_id}/rate", tags=["Rating"])
def rate_artist(artist_id: str, rating: Rating):
    if artist_id not in artists_db:
        raise HTTPException(status_code=404, detail="Artist not found")
    rating_id = str(uuid4())
    ratings_db[rating_id] = {"artist_id": artist_id, "rating": rating}
    return {"id": rating_id, "rating": rating}

@app.get("/rating/artists/{artist_id}/ratings", tags=["Rating"])
def get_ratings_for_artist(artist_id: str):
    artist_ratings = [rating for rating in ratings_db.values() if rating["artist_id"] == artist_id]
    return artist_ratings

@app.put("/rating/artists/{artist_id}/ratings/{rating_id}", tags=["Rating"])
def update_rating(artist_id: str, rating_id: str, rating: Rating):
    if rating_id not in ratings_db:
        raise HTTPException(status_code=404, detail="Rating not found")
    ratings_db[rating_id] = {"artist_id": artist_id, "rating": rating}
    return {"id": rating_id, "rating": rating}

@app.delete("/rating/{artist_id}/ratings/{rating_id}", tags=["Rating"])
def delete_rating(artist_id: str, rating_id: str):
    if rating_id not in ratings_db:
        raise HTTPException(status_code=404, detail="Rating not found")
    del ratings_db[rating_id]
    return {"message": "Rating deleted"}

@app.get("/rating/{artist_id}/ratings/{rating_id}", tags=["Rating"])
def get_rating(artist_id: str, rating_id: str):
    if rating_id not in ratings_db:
        raise HTTPException(status_code=404, detail="Rating not found")
    return ratings_db[rating_id]

# Stage Management Endpoints
@app.get("/stages/", tags=["Stage Management"])
def get_stages():
    return list(stages_db.values())

@app.get("/stages/{id}", tags=["Stage Management"])
def get_stage(id: str):
    if id not in stages_db:
        raise HTTPException(status_code=404, detail="Stage not found")
    return stages_db[id]

@app.post("/stages/", tags=["Stage Management"])
def add_stage(stage: Stage):
    stage_id = str(uuid4())
    stages_db[stage_id] = stage
    return {"id": stage_id, "stage": stage}

@app.put("/stages/{id}", tags=["Stage Management"])
def update_stage(id: str, stage: Stage):
    if id not in stages_db:
        raise HTTPException(status_code=404, detail="Stage not found")
    stages_db[id] = stage
    return {"id": id, "stage": stage}

@app.delete("/stages/{id}", tags=["Stage Management"])
def delete_stage(id: str):
    if id not in stages_db:
        raise HTTPException(status_code=404, detail="Stage not found")
    del stages_db[id]
    return {"message": "Stage deleted"}

# Schedule Management Endpoints
@app.get("/schedule/", tags=["Schedule Management"])
def get_schedule():
    return list(schedule_db.values())

@app.get("/schedule/{day}", tags=["Schedule Management"])
def get_schedule_for_day(day: str):
    day_schedule = [entry for entry in schedule_db.values() if entry["day"] == day]
    return day_schedule

@app.post("/schedule/", tags=["Schedule Management"])
def create_schedule_entry(schedule: Schedule):
    schedule_id = str(uuid4())
    schedule_db[schedule_id] = schedule
    return {"id": schedule_id, "schedule": schedule}

@app.put("/schedule/{id}", tags=["Schedule Management"])
def update_schedule_entry(id: str, schedule: Schedule):
    if id not in schedule_db:
        raise HTTPException(status_code=404, detail="Schedule entry not found")
    schedule_db[id] = schedule
    return {"id": id, "schedule": schedule}

@app.delete("/schedule/{id}", tags=["Schedule Management"])
def delete_schedule_entry(id: str):
    if id not in schedule_db:
        raise HTTPException(status_code=404, detail="Schedule entry not found")
    del schedule_db[id]
    return {"message": "Schedule entry deleted"}

# Ticket Management Endpoints
@app.get("/tickets/", tags=["Ticket Management"])
def get_tickets():
    return list(tickets_db.values())

@app.post("/tickets/purchase/", tags=["Ticket Management"])
def purchase_ticket(ticket: Ticket):
    ticket_id = str(uuid4())
    tickets_db[ticket_id] = ticket
    return {"id": ticket_id, "ticket": ticket}

@app.get("/tickets/report/", tags=["Ticket Management"])
def get_ticket_sales_report():
    return {"message": "Sales report (mock data)"}

# User Management Endpoints
@app.post("/users/register/", tags=["User Management"])
def register_user(user: User):
    user_id = str(uuid4())
    users_db[user_id] = user
    return {"id": user_id, "user": user}

@app.get("/users/{user_id}/", tags=["User Management"])
def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.put("/users/{user_id}", tags=["User Management"])
def update_user(user_id: str, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {"id": user_id, "user": user}

# User Profile Endpoints
@app.get("/profile/{user_id}/", tags=["User Profile"])
def get_user_profile(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"profile": users_db[user_id]}

@app.put("/profile/{user_id}/", tags=["User Profile"])
def update_user_profile(user_id: str, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {"id": user_id, "profile": user}

# Health Check Endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "API is up and running"}
