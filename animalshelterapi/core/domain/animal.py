"""Module containing animal-related domain models."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AnimalIn(BaseModel):
    """Model representing animal's DTO attributes."""
    name: str
    species: str
    breed: str
    age: int
    gender: str
    arrival_date: date
    adoption_status: str
    description: Optional[str] = None


class Animal(AnimalIn):
    """Model representing animal's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")