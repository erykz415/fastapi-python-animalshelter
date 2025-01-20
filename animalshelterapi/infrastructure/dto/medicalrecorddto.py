"""A module containing DTO models for output medical records."""


from datetime import date
from typing import Optional
from asyncpg import Record  # type: ignore
from pydantic import BaseModel, ConfigDict

from animalshelterapi.infrastructure.dto.animaldto import AnimalDTO


class MedicalRecordDTO(BaseModel):
    """A model representing DTO for medical record data."""
    id: int
    animal: AnimalDTO
    visit_date: date
    diagnosis: str
    treatment: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> "MedicalRecordDTO":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            AirportDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            animal=AnimalDTO(
                id=record_dict.get("id_1"),
                name=record_dict.get("name"),
                species=record_dict.get("species"),
                breed=record_dict.get("breed"),
                age=record_dict.get("age"),
                gender=record_dict.get("gender"),
                arrival_date=record_dict.get("arrival_date"),
                adoption_status=record_dict.get("adoption_status"),
                description=record_dict.get("description"),
            ),
            visit_date = record_dict.get("visit_date"),
            diagnosis = record_dict.get("diagnosis"),
            treatment = record_dict.get("treatment"),
        )
