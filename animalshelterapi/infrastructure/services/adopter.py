
"""Module containing continent service implementation."""

from typing import Iterable


from animalshelterapi.core.domain.adoption import Adopter, AdopterIn
from animalshelterapi.core.repositories.iadopter import IAdopterRepository
from animalshelterapi.infrastructure.services.iadopter import IAdopterService
from animalshelterapi.infrastructure.services.ianimal import IAnimalService


class AdopterService(IAdopterService):
    """A class implementing the continent service."""

    _repository: IAdopterRepository

    def __init__(self, repository: IAdopterRepository) -> None:
        """The initializer of the `Adopter service`.

        Args:
            repository (IAdopterRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_adopter_by_id(self, adopter_id: int) -> Adopter | None:
        """The method getting an adopter from the repository.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Adopter | None: The adopter data if exists.
        """

        return await self._repository.get_adopter_by_id(adopter_id)

    async def get_adopter_by_last_name(self, last_name: str) -> Iterable[Adopter]:
        """The method getting an adopter from the repository.

        Args:
            last_name (str): The last name of the adopter.

        Returns:
            Iterable[Adopter]: The adopter data if exists.
        """

        return await self._repository.get_adopter_by_last_name(last_name)

    async def get_adopter_by_phone_number(self, phone_number: str) -> Iterable[Adopter]:
        """The method getting an adopter from the repository.

        Args:
            phone_number (str): The phone number of the adopter.

        Returns:
            Iterable[Adopter]: The adopter data if exists.
        """

        return await self._repository.get_adopter_by_phone_number(phone_number)

    async def get_all_adopters(self) -> Iterable[Adopter]:
        """The method getting all adopters from the repository.

        Returns:
            Iterable[Adopter]: The collection of the all adopters.
        """

        return await self._repository.get_all_adopters()

    async def add_adopter(self, data: AdopterIn) -> Adopter | None:
        """The method adding new adopter to the repository.

        Args:
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Adopter | None: The newly created adopter.
        """

        return await self._repository.add_adopter(data)

    async def update_adopter(
        self,
        adopter_id: int,
        data: AdopterIn,
    ) -> Adopter | None:
        """The method updating adopter data in the repository.

        Args:
            adopter_id (int): The adopter id.
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Adopter | None: The updated continent.
        """

        return await self._repository.update_adopter(
            adopter_id=adopter_id,
            data=data,
        )

    async def delete_adopter(self, adopter_id: int) -> bool:
        """The method removing adopter from the repository.

        Args:
            adopter_id (int): The adopter id.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_adopter(adopter_id)
