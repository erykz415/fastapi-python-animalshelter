"""Module containing adopter service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from animalshelterapi.core.domain.adoption import Adopter, AdopterIn


class IAdopterService(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_adopter_by_id(self, adopter_id: int) -> Adopter | None:
        """The abstract getting an adopter from the repository.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Adopter | None: The adopter data if exists.
        """

    @abstractmethod
    async def get_adopter_by_last_name(self, last_name: str) -> Iterable[Adopter]:
        """The abstract getting an adopter from the repository.

        Args:
            last_name (int): The last name of the adopter.

        Returns:
            Adopter | None: The adopter data if exists.
        """

    @abstractmethod
    async def get_adopter_by_phone_number(self, phone_number: str) -> Iterable[Adopter]:
        """The abstract getting an adopter from the repository.

        Args:
            phone_number (str): The phone number of the adopter.

        Returns:
            Iterable[Adopter]: The adopter data if exists.
        """

    @abstractmethod
    async def get_all_adopters(self) -> Iterable[Adopter]:
        """The abstract getting all adopters from the repository.

        Returns:
            Iterable[Adopter]: The collection of the all adopters.
        """

    @abstractmethod
    async def add_adopter(self, data: AdopterIn) -> Adopter | None:
        """The abstract adding new adopter to the repository.

        Args:
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Adopter | None: The newly created adopter.
        """

    @abstractmethod
    async def update_adopter(
        self,
        adopter_id: int,
        data: AdopterIn,
    ) -> Adopter | None:
        """The abstract updating adopter data in the repository.

        Args:
            adopter_id (int): The adopter id.
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Adopter | None: The updated adopter.
        """

    @abstractmethod
    async def delete_adopter(self, adopter_id: int) -> bool:
        """The abstract removing adopter from the repository.

        Args:
            adopter_id (int): The adopter id.

        Returns:
            bool: Success of the operation.
        """
