"""A module containing DTO models for adopter."""


from pydantic import BaseModel, ConfigDict  # type: ignore


class AdopterDTO(BaseModel):
    """A model representing DTO for adopter data."""
    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
