from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from .user_model import User

class Task(Document):
    task_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str) # type: ignore
    description: Indexed(str) # type: ignore
    created_at: datetime = Field(default_factory=datetime.utcnow())
    updated_at: datetime = Field(default_factory=datetime.utcnow())
    owner: Link[User]

    def __repr__(self) -> str:
        return f'Task {self.title}'
    
    def __str__(self) -> str:
        return self.title
    
    def __hash__(self) -> int:
        return hash(self.title)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False
    
    @before_event([Replace, Insert])
    def sync_update(self):
        self.updated_at = datetime.now(datetime.UTC)