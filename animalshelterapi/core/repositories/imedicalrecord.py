"""Module containing medical record repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from animalshelterapi.core.domain.medicalrecord import MedicalRecordIn


class IMedicalRecordRepository(ABC):
    """An abstract class representing protocol of medical record repository."""

    @abstractmethod
    async def get_medical_record_by_id(self, medical_record_d: int) -> Any | None:
        """The abstract getting a medical record from the data storage.

        Args:
            medical_record_d (int): The id of the medical record.

        Returns:
            Any | None: The medical record data if exists.
        """

    @abstractmethod
    async def get_all_medical_records(self) -> Iterable[Any]:
        """The abstract getting all medical records from the data storage.

        Returns:
            Iterable[Any]: The collection of the all medical records.
        """

    @abstractmethod
    async def get_medical_record_by_animal_id(
        self,
        animal_id: int,
    ) -> Iterable[Any]:
        """The abstract getting all provided animal's medical records
            from the data storage.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[Any]: The collection of the medical records.
        """

    @abstractmethod
    async def add_medical_record(self, data: MedicalRecordIn) -> Any | None:
        """The abstract adding new medical record to the data storage.

        Args:
            data (MedicalRecordIn): The attributes of the medical record.

        Returns:
            Any | None: The newly created medical record.
        """

    @abstractmethod
    async def update_medical_record(
        self,
        medical_record_id: int,
        data: MedicalRecordIn,
    ) -> Any | None:
        """The abstract updating medical record data in the data storage.

        Args:
            medical_record_id (int): The medical record id.
            data (MedicalRecordIn): The attributes of the medical record.

        Returns:
            Any | None: The updated medical record.
        """

    @abstractmethod
    async def delete_medical_record(self, medical_record_id: int) -> bool:
        """The abstract removing medical record from the data storage.

        Args:
            medical_record_id (int): The medical record id.

        Returns:
            bool: Success of the operation.
        """
