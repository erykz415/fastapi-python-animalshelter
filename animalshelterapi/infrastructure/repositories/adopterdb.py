"""Module containing adopter database repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from animalshelterapi.core.domain.adoption import Adopter, AdopterIn
from animalshelterapi.core.repositories.iadopter import IAdopterRepository
from animalshelterapi.db import adopter_table, database


class AdopterRepository(IAdopterRepository):
    """A class implementing the adopter repository."""

    async def get_adopter_by_id(self, adopter_id: int) -> Any | None:
        """The method getting an adopter from the data storage.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Any | None: The adopter data if exists.
        """

        adopter = await self._get_by_id(adopter_id)

        return Adopter(**dict(adopter)) if adopter else None

    async def get_adopter_by_last_name(self, last_name: str) -> Iterable[Any]:
        """The method getting an adopter from the data storage.

        Args:
            last_name (str): The last name of the adopter.

        Returns:
            Iterable[Any]: The collection of the adopters.
        """

        query = adopter_table.select().where(adopter_table.c.last_name == last_name).order_by(adopter_table.c.id.asc())
        adopters = await database.fetch_all(query)

        return [Adopter(**dict(adopter)) for adopter in adopters]

    async def get_adopter_by_phone_number(self, phone_number: str) -> Iterable[Any]:
        """The method getting an adopter from the data storage.

        Args:
            phone_number (str): The phone number of the adopter.

        Returns:
            Iterable[Any]: The collection of the adopters.
        """

        query = adopter_table.select().where(adopter_table.c.phone_number == phone_number).order_by(adopter_table.c.id.asc())
        adopters = await database.fetch_all(query)

        return [Adopter(**dict(adopter)) for adopter in adopters]

    async def get_all_adopters(self) -> Iterable[Any]:
        """The method getting all adopters from the data storage.

        Returns:
            Iterable[Any]: The collection of the all adopters.
        """

        query = adopter_table.select().order_by(adopter_table.c.id.asc())
        adopters = await database.fetch_all(query)

        return [Adopter(**dict(adopter)) for adopter in adopters]

    async def add_adopter(self, data: AdopterIn) -> Any | None:
        """The method adding new adopter to the data storage.

        Args:
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Any | None: The newly created adopter.
        """

        query = adopter_table.insert().values(**data.model_dump())
        new_adopter_id = await database.execute(query)
        new_adopter = await self._get_by_id(new_adopter_id)

        return Adopter(**dict(new_adopter)) if new_adopter else None

    async def update_adopter(
        self,
        adopter_id: int,
        data: AdopterIn,
    ) -> Any | None:
        """The method updating adopter data in the data storage.

        Args:
            adopter_id (int): The adopter id.
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Any | None: The updated adopter.
        """

        if self._get_by_id(adopter_id):
            query = (
                adopter_table.update()
                .where(adopter_table.c.id == adopter_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            adopter = await self._get_by_id(adopter_id)

            return Adopter(**dict(adopter)) if adopter else None

        return None

    async def delete_adopter(self, adopter_id: int) -> bool:
        """The method removing adopter from the data storage.

        Args:
            adopter_id (int): The adopter id.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(adopter_id):
            query = adopter_table \
                .delete() \
                .where(adopter_table.c.id == adopter_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, adopter_id: int) -> Record | None:
        """A private method getting adopter from the DB based on its ID.

        Args:
            adopter_id (int): The ID of the adopter.

        Returns:
            Any | None: Adopter record if exists.
        """

        query = (
            adopter_table.select()
            .where(adopter_table.c.id == adopter_id)
            .order_by(adopter_table.c.id.asc())
        )

        return await database.fetch_one(query)
