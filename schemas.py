from pydantic import BaseModel, ConfigDict
from typing import Optional


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class STask(STaskAdd):
    id:int

class Config:
        from_attributes = True


class STaskId(BaseModel):
    ok: bool = True
    task_id: int 
