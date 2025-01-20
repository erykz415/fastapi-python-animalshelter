"""Module containing medical record repository implementation."""

from typing import Iterable

from animalshelterapi.core.repositories.imedicalrecord import IMedicalRecordRepository
from animalshelterapi.core.domain.medicalrecord import MedicalRecord, MedicalRecordIn
from animalshelterapi.infrastructure.repositories.db import medical_records


class MedicalRecordMockRepository(IMedicalRecordRepository):
    """A class representing medical record repository."""

    async def get_all_medical_records(self) -> Iterable[MedicalRecord]:
        """The method getting all medical records from the data storage.

        Returns:
            Iterable[MedicalRecord]: Medical records in the data storage.
        """

        return medical_records

    async def get_medical_record_by_animal_id(self, animal_id: int) -> Iterable[MedicalRecord]:
        """The method getting medical records assigned to particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[MedicalRecord]: Medical records assigned to a country.
        """

        return list(filter(lambda x: x.animal_id == animal_id, medical_records))

    async def get_medical_record_by_id(self, medical_record_id: int) -> MedicalRecord | None:
        """The method getting medical record by provided id.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            MedicalRecord | None: The medical record details.
        """

        return next((obj for obj in medical_records if obj.id == medical_record_id), None)


    async def add_medical_record(self, data: MedicalRecordIn) -> None:
        """The method adding new medical record to the data storage.

        Args:
            data (MedicalRecordIn): The details of the new medical record.

        Returns:
            Airport: Full details of the newly added medical record.
        """

        medical_records.append(data)

    async def update_medical_record(
        self,
        medical_record_id: int,
        data: MedicalRecordIn,
    ) -> MedicalRecord | None:
        """The method updating medical record data in the data storage.

        Args:
            medical_record_id (int): The id of the medical record.
            data (MedicalRecordIn): The details of the updated medical record.

        Returns:
            MedicalRecord | None: The updated medical record details.
        """

        if medical_record_pos := \
                next(filter(lambda x: x.id == medical_record_id, medical_records)):
            medical_records[medical_record_pos] = data

            return MedicalRecord(id=0, **data.model_dump())

        return None

    async def delete_medical_record(self, medical_record_id: int) -> bool:
        """The method removing medical record from the data storage.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            bool: Success of the operation.
        """

        if medical_record_pos := \
                next(filter(lambda x: x.id == medical_record_id, medical_records)):
            medical_records.remove(medical_record_pos)
            return True

        return False
