import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models import JobStatus


class JobCreate(BaseModel):
    # Mijoz faqat title yuboradi; id, status va vaqtni server beradi.
    title: str = Field(min_length=1, max_length=200)


class JobOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    status: JobStatus
    created_at: datetime
