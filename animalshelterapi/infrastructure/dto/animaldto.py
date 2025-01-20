"""A module containing DTO models for animal."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict  # type: ignore


class AnimalDTO(BaseModel):
    """A model representing DTO for animal data."""
    id: int
    name: str
    species: str
    breed: str
    age: int
    gender: str
    arrival_date: date
    adoption_status: str
    description: Optional[str]=None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
