import uuid
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    username: str
    email: str
    password: str
    role: str  # bilo koji string: USER, SUPPORT, ADMIN

class Ticket(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    description: str
    status: str
    priority: str | None = None
    created_at: str  # string za jednostavnost
    created_by: str  # ID od Usera
    assigned_to: str | None = None  # ID od supporta

class Attachment(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    file_name: str
    file_path: str
    ticket_id: str  # ID od Ticket