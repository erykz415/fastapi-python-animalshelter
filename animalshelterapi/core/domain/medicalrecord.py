"""Module containing medical record-related domain models."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MedicalRecordIn(BaseModel):
    """Model representing medical record's DTO attributes."""
    animal_id: int
    visit_date: date
    diagnosis: str
    treatment: Optional[str] = None


class MedicalRecord(MedicalRecordIn):
    """Model representing medical record's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

