
"""Module containing airport repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from animalshelterapi.core.repositories.imedicalrecord import IMedicalRecordRepository
from animalshelterapi.core.domain.medicalrecord import MedicalRecord, MedicalRecordIn
from animalshelterapi.db import (
    animal_table,
    medical_record_table,
    database,
)
from animalshelterapi.infrastructure.dto.medicalrecorddto import MedicalRecordDTO


class MedicalRecordRepository(IMedicalRecordRepository):
    """A class representing continent DB repository."""

    async def get_all_medical_records(self) -> Iterable[Any]:
        """The method getting all airports from the data storage.

        Returns:
            Iterable[Any]: Airports in the data storage.
        """

        query = (
            select(medical_record_table, animal_table)
            .select_from(
                join(
                    medical_record_table,
                    animal_table,
                    medical_record_table.c.animal_id == animal_table.c.id
                )
            )
            .order_by(medical_record_table.c.id.asc())
        )
        medical_records = await database.fetch_all(query)

        return [MedicalRecordDTO.from_record(medical_record) for medical_record in medical_records]

    async def get_medical_record_by_animal_id(self, animal_id: int) -> Iterable[Any]:
        """The method getting airports assigned to particular country.

        Args:
            animal_id (int): The id of the country.

        Returns:
            Iterable[Any]: Airports assigned to a country.
        """

        query = (
            select(medical_record_table, animal_table)
            .select_from(
                join(
                    medical_record_table,
                    animal_table,
                    medical_record_table.c.animal_id == animal_table.c.id
                )
            )
            .where(medical_record_table.c.animal_id == animal_id)
            .order_by(medical_record_table.c.id.asc())
        )

        medical_records = await database.fetch_all(query)

        return [MedicalRecordDTO.from_record(medical_record) for medical_record in medical_records]


    async def get_medical_record_by_id(self, medical_record_id: int) -> Any | None:
        """The method getting medical record by provided id.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            Any | None: The medical record details.
        """

        query = (
            select(medical_record_table, animal_table)
            .select_from(
                join(
                    medical_record_table,
                    animal_table,
                    medical_record_table.c.animal_id == animal_table.c.id
                )
            )
            .where(medical_record_table.c.id == medical_record_id)
            .order_by(medical_record_table.c.id.asc())
        )
        medical_record = await database.fetch_one(query)

        return MedicalRecordDTO.from_record(medical_record) if medical_record else None

    async def add_medical_record(self, data: MedicalRecordIn) -> Any | None:
        """The method adding new medical record to the data storage.

        Args:
            data (MedicalRecordIn): The details of the new medical record.

        Returns:
            MedicalRecord: Full details of the newly added medical record.

        Returns:
            Any | None: The newly added medical record.
        """

        query = medical_record_table.insert().values(**data.model_dump())
        new_medical_record_id = await database.execute(query)
        new_medical_record = await self._get_by_id(new_medical_record_id)

        return MedicalRecord(**dict(new_medical_record)) if new_medical_record else None

    async def update_medical_record(
        self,
        medical_record_id: int,
        data: MedicalRecordIn,
    ) -> Any | None:
        """The method updating medical record data in the data storage.

        Args:
            medical_record_id (int): The id of the medical record.
            data (MedicalRecordIn): The details of the updated medical record.

        Returns:
            Any | None: The updated medical record details.
        """

        if self._get_by_id(medical_record_id):
            query = (
                medical_record_table.update()
                .where(medical_record_table.c.id == medical_record_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            medical_record = await self._get_by_id(medical_record_id)

            return MedicalRecord(**dict(medical_record)) if medical_record else None

        return None

    async def delete_medical_record(self, medical_record_id: int) -> bool:
        """The method removing medical record from the data storage.

        Args:
            medical_record_id (int): The id of the medical record.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(medical_record_id):
            query = medical_record_table \
                .delete() \
                .where(medical_record_table.c.id == medical_record_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, medical_record_id: int) -> Record | None:
        """A private method getting medical record from the DB based on its ID.

        Args:
            medical_record_id (int): The ID of the medical record.

        Returns:
            Any | None: Medical record if exists.
        """

        query = (
            medical_record_table.select()
            .where(medical_record_table.c.id == medical_record_id)
            .order_by(medical_record_table.c.id.asc())
        )

        return await database.fetch_one(query)
