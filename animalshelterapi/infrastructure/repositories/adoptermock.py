"""Module containing adopter repository implementation."""

from typing import Iterable

from animalshelterapi.core.domain.adoption import Adopter, AdopterIn
from animalshelterapi.core.repositories.iadopter import IAdopterRepository
from animalshelterapi.infrastructure.repositories.db import adopters


class AdopterRepository(IAdopterRepository):
    """A class implementing the adopter repository."""

    async def get_adopter_by_id(self, adopter_id: int) -> Adopter | None:
        """The method getting an adopter from the data storage.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Adopter | None: The adopter data if exists.
        """

        return next(
            (obj for obj in adopters if obj.id == adopter_id),
            None,
        )

    async def get_adopter_by_last_name(self, last_name: str) -> Iterable[Adopter]:
        """The method getting adopters from the data storage.

        Args:
            last_name (str): The last name of the adopter.

        Returns:
            Iterable[Adopter]: The adopter data if exists.
        """

        return (obj for obj in adopters if obj.last_name == last_name)

    async def get_adopter_by_phone_number(self, phone_number: str) -> Iterable[Adopter]:
        """The method getting adopters from the data storage.

        Args:
            phone_number (str): The phone number of the adopter.

        Returns:
            Iterable[Adopter]: The adopter data if exists.
        """

        return (obj for obj in adopters if obj.phone_number == phone_number)


    async def get_all_adopters(self) -> Iterable[Adopter]:
        """The method getting all adopters from the data storage.

        Returns:
            Iterable[Adopter]: The collection of the all adopters.
        """

        return adopters

    async def add_adopter(self, data: AdopterIn) -> None:
        """The method adding new adopter to the data storage.

        Args:
            data (AdopterIn): The attributes of the adopter.
        """

        adopters.append(data)

    async def update_adopter(
        self,
        adopter_id: int,
        data: AdopterIn,
    ) -> Adopter | None:
        """The method updating adopter data in the data storage.

        Args:
            adopter_id (int): The adopter id.
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Adopter | None: The updated adopter.
        """

        if adopter_pos := \
                next(filter(lambda x: x.id == adopter_id, adopters)):
            adopters[adopter_pos] = data

            return Adopter(id=0, **data.model_dump())

        return None

    async def delete_adopter(self, adopter_id: int) -> bool:
        """The method removing adopter from the data storage.

        Args:
            adopter_id (int): The adopter id.

        Returns:
            bool: Success of the operation.
        """

        if adopter_pos := \
                next(filter(lambda x: x.id == adopter_id, adopters)):
            adopters.remove(adopter_pos)
            return True

        return False
