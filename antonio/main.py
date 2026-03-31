from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from models import User, Ticket, Attachment
from pydantic import BaseModel

# SQLite baza
engine = create_engine("sqlite:///database.db")

# Kreiranje tablica
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API radi 🚀"}

# Pydantic model za unos ticketa
class TicketCreate(BaseModel):
    title: str
    description: str
    status: str
    priority: str | None = None
    created_at: str
    created_by: str
    assigned_to: str | None = None

# Endpoint za kreiranje ticketa
@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        status=ticket.status,
        priority=ticket.priority,
        created_at=ticket.created_at,
        created_by=ticket.created_by,
        assigned_to=ticket.assigned_to
    )
    with Session(engine) as session:
        session.add(db_ticket)
        session.commit()
        session.refresh(db_ticket)
    return {"message": "Ticket zaprimljen!", "ticket_id": db_ticket.id}

# Endpoint za kreiranje korisnika (za testiranje)
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str

@app.post("/users")
def create_user(user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        role=user.role
    )
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return {"message": "User dodan!", "user_id": db_user.id}