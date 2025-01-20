"""Module containing medical record service implementation."""

from typing import Iterable

from animalshelterapi.core.domain.medicalrecord import MedicalRecord, MedicalRecordIn
from animalshelterapi.core.repositories.imedicalrecord import IMedicalRecordRepository
from animalshelterapi.infrastructure.services.imedicalrecord import IMedicalRecordService


class MedicalRecordService(IMedicalRecordService):
    """A class implementing the country service."""

    _repository: IMedicalRecordRepository

    def __init__(self, repository: IMedicalRecordRepository) -> None:
        """The initializer of the `medical record service`.

        Args:
            repository (IMedicalRecordRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_medical_record_by_id(self, medical_record_id: int) -> MedicalRecord | None:
        """The abstract getting a medical record from the repository.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            MedicalRecord | None: The medical record data if exists.
        """

        return await self._repository.get_medical_record_by_id(medical_record_id)

    async def get_all_medical_records(self) -> Iterable[MedicalRecord]:
        """The abstract getting all medical records from the repository.

        Returns:
            Iterable[MedicalRecord]: The collection of the all medical records.
        """

        return await self._repository.get_all_medical_records()

    async def get_medical_record_by_animal_id(
        self,
        animal_id: int,
    ) -> Iterable[MedicalRecord]:
        """The abstract getting all provided animal's medical records
            from the repository.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[MedicalRecord]: The collection of the medical records.
        """

        return await self._repository.get_medical_record_by_animal_id(animal_id)

    async def add_medical_record(self, data: MedicalRecordIn) -> MedicalRecord | None:
        """The abstract adding new medical record to the repository.

        Args:
            data (MedicalRecordIn): The attributes of the medical record.

        Returns:
            MedicalRecord | None: The newly created medical record.
        """

        return await self._repository.add_medical_record(data)

    async def update_medical_record(
        self,
        medical_record_id: int,
        data: MedicalRecordIn,
    ) -> MedicalRecord | None:
        """The abstract updating medical record data in the repository.

        Args:
            medical_record_id (int): The medical record id.
            data (MedicalRecordIn): The attributes of the medical record.

        Returns:
            MedicalRecord | None: The updated medical record.
        """

        return await self._repository.update_medical_record(
            medical_record_id=medical_record_id,
            data=data,
        )

    async def delete_medical_record(self, medical_record_id: int) -> bool:
        """The abstract removing medical record from the repository.

        Args:
            medical_record_id (int): The medical record id.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_medical_record(medical_record_id)
