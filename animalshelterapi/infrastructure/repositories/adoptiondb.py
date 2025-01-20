"""Module containing adoption repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from animalshelterapi.core.repositories.iadoption import IAdoptionRepository
from animalshelterapi.core.domain.adoption import Adoption, AdoptionIn
from animalshelterapi.db import (
    animal_table,
    adopter_table,
    adoption_table,
    database,
)
from animalshelterapi.infrastructure.dto.adoptiondto import AdoptionDTO


class AdoptionRepository(IAdoptionRepository):
    """A class representing continent DB repository."""

    async def get_all_adoptions(self) -> Iterable[Any]:
        """The method getting all adoptions from the data storage.

        Returns:
            Iterable[Any]: Adoptions in the data storage.
        """

        query = (
            select(
                adoption_table,
                animal_table,
                adopter_table
            )
            .select_from(
                join(
                    adoption_table,
                    adopter_table,
                    adoption_table.c.adopter_id == adopter_table.c.id
                ).join(
                    animal_table,
                    adoption_table.c.animal_id == animal_table.c.id
                )
            )
            .order_by(adoption_table.c.id.asc())
        )
        adoptions = await database.fetch_all(query)

        return [AdoptionDTO.from_record(adoption) for adoption in adoptions]

    async def get_by_animal_id(self, animal_id: int) -> Iterable[Any]:
        """The method getting adoption assigned to a particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[Any]: Adoption assigned to an animal.
        """

        query = adoption_table \
            .select() \
            .where(adoption_table.c.animal_id == animal_id) \

        adoptions = await database.fetch_all(query)

        return [Adoption(**dict(adoption)) for adoption in adoptions]

    async def get_by_adopter_id(self, adopter_id: int) -> Iterable[Any]:
        """The method getting adoptions assigned to particular adopter.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Iterable[Any]: Adoptions assigned to an adopter.
        """

        query = adoption_table \
            .select() \
            .where(adoption_table.c.adopter_id == adopter_id) \
            .order_by(adoption_table.c.id.asc())

        adoptions = await database.fetch_all(query)

        return [Adoption(**dict(adoption)) for adoption in adoptions]

    async def get_by_id(self, adoption_id: int) -> Any | None:
        """The method getting adoption by provided id.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            Any | None: The adoption details.
        """

        query = (
            select(
                adoption_table,
                animal_table,
                adopter_table
            )
            .select_from(
                join(
                    adoption_table,
                    adopter_table,
                    adoption_table.c.adopter_id == adopter_table.c.id
                ).join(
                    animal_table,
                    adoption_table.c.animal_id == animal_table.c.id
                )
            )
            .order_by(adoption_table.c.id.asc())
            .where(adoption_table.c.id == adoption_id))

        adoption = await database.fetch_one(query)

        return AdoptionDTO.from_record(adoption) if adoption else None

    async def add_adoption(self, data: AdoptionIn) -> Any | None:
        """The method adding new adoption to the data storage.

        Args:
            data (AdoptionIn): The details of the new adoption.

        Returns:
            Any | None: The newly added adoption.
        """

        query = adoption_table.insert().values(**data.model_dump())
        new_adoption_id = await database.execute(query)
        new_adoption = await self._get_by_id(new_adoption_id)

        return Adoption(**dict(new_adoption)) if new_adoption else None

    async def update_adoption(
        self,
        adoption_id: int,
        data: AdoptionIn,
    ) -> Any | None:
        """The method updating adoption data in the data storage.

        Args:
            adoption_id (int): The id of the adoption.
            data (AdoptionIn): The details of the updated adoption.

        Returns:
            Any | None: The updated adoption details.
        """

        if self._get_by_id(adoption_id):
            query = (
                adoption_table.update()
                .where(adoption_table.c.id == adoption_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            adoption = await self._get_by_id(adoption_id)

            return Adoption(**dict(adoption)) if adoption else None

        return None

    async def delete_adoption(self, adoption_id: int) -> bool:
        """The method removing adoption from the data storage.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(adoption_id):
            query = adoption_table \
                .delete() \
                .where(adoption_table.c.id == adoption_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, adoption_id: int) -> Record | None:
        """A private method getting adoption from the DB based on its ID.

        Args:
            adoption_id (int): The ID of the adoption.

        Returns:
            Any | None: Adoption record if exists.
        """

        query = (
            adoption_table.select()
            .where(adoption_table.c.id == adoption_id)
            .order_by(adoption_table.c.id.asc())
        )

        return await database.fetch_one(query)
