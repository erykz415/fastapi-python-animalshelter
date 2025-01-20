"""A module containing DTO models for output adoptions."""


from datetime import date
from asyncpg import Record  # type: ignore
from pydantic import BaseModel, ConfigDict

from animalshelterapi.infrastructure.dto.adopterdto import AdopterDTO
from animalshelterapi.infrastructure.dto.animaldto import AnimalDTO


class AdoptionDTO(BaseModel):
    """A model representing DTO for adoption data."""
    id: int
    animal: AnimalDTO
    adopter: AdopterDTO
    adoption_date: date

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> "AdoptionDTO":
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
            adopter=AdopterDTO(
                id=record_dict.get("id_2"),
                first_name=record_dict.get("first_name"),
                last_name=record_dict.get("last_name"),
                phone_number=record_dict.get("phone_number"),
                email=record_dict.get("email"),
                address=record_dict.get("address"),
            ),
            adoption_date=record_dict.get("adoption_date"),
        )
