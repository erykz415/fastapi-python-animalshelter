"""Module containing adoption-related domain models."""

from datetime import date
from pydantic import BaseModel, ConfigDict


class AdoptionIn(BaseModel):
    """Model representing adoption's DTO attributes."""
    animal_id: int
    adopter_id: int
    adoption_date: date


class Adoption(AdoptionIn):
    """Model representing adoption's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")


class AdopterIn(BaseModel):
    """Model representing adopter's DTO attributes."""
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str


class Adopter(AdopterIn):
    """Model representing adopter's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
