from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, Dict

class ReportDTO(BaseModel):
    """A model representing DTO for report data."""
    id: int
    topic: str
    content: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Dict[str, Any]) -> 'ReportDTO':
        """Creates an instance of ReportDTO from a record (typically a dictionary)."""
        # Add defaults for missing fields if necessary or handle them accordingly
        if 'id' not in record:
            record['id'] = 0  # Default value for 'id'
        if 'created_at' not in record:
            record['created_at'] = datetime.now()  # Default to current timestamp if missing

        return cls(**record)
