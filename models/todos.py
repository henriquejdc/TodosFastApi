from pydantic import BaseModel


class Todo(BaseModel):
    id: str = None
    name: str
    description: str
    completed: bool
