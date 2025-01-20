"""Module containing medical record service abstractions."""

from abc import ABC, abstractmethod

from typing import Iterable

from animalshelterapi.core.domain.medicalrecord import MedicalRecord, MedicalRecordIn


class IMedicalRecordService(ABC):
    """An abstract class representing protocol of medical record repository."""

    @abstractmethod
    async def get_medical_record_by_id(self, medical_record_id: int) -> MedicalRecord | None:
        """The abstract getting a medical record from the repository.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            MedicalRecord | None: The medical record data if exists.
        """

    @abstractmethod
    async def get_all_medical_records(self) -> Iterable[MedicalRecord]:
        """The abstract getting all medical records from the repository.

        Returns:
            Iterable[MedicalRecord]: The collection of the all medical records.
        """

    @abstractmethod
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

    @abstractmethod
    async def add_medical_record(self, data: MedicalRecordIn) -> MedicalRecord | None:
        """The abstract adding new medical record to the repository.

        Args:
            data (MedicalRecordIn): The attributes of the medical record.

        Returns:
            MedicalRecord | None: The newly created medical record.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_medical_record(self, medical_record_id: int) -> bool:
        """The abstract removing medical record from the repository.

        Args:
            medical_record_id (int): The medical record id.

        Returns:
            bool: Success of the operation.
        """
