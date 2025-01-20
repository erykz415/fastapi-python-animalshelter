"""Module containing report-related domain models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ReportIn(BaseModel):
    """Model representing report's DTO attributes."""
    topic: str
    content: str
    created_at: datetime


class Report(ReportIn):
    """Model representing report's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")