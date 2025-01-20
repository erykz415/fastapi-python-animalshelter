"""Module containing adopter repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from animalshelterapi.core.domain.adoption import AdopterIn


class IAdopterRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_adopter_by_id(self, adopter_id: int) -> Any | None:
        """The abstract getting an adopter from the data storage.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Any | None: The adopter data if exists.
        """

    @abstractmethod
    async def get_adopter_by_last_name(self, last_name: str) -> Iterable[Any]:
        """The abstract getting an adopter from the data storage.

        Args:
            last_name (str): The last name of the adopter.

        Returns:
            Iterable[Any]: The collection of the adopters.
        """

    @abstractmethod
    async def get_adopter_by_phone_number(self, phone_number: str) -> Iterable[Any]:
        """The abstract getting an adopter from the data storage.

        Args:
            phone_number (str): The phone number of the adopter.

        Returns:
            Iterable[Any]: The collection of the adopters.
        """

    @abstractmethod
    async def get_all_adopters(self) -> Iterable[Any]:
        """The abstract getting all adopters from the data storage.

        Returns:
            Iterable[Any]: The collection of the all adopters.
        """

    @abstractmethod
    async def add_adopter(self, data: AdopterIn) -> Any | None:
        """The abstract adding new adopter to the data storage.

        Args:
            data (AdopterIn): The attributes of the adopter.

        Returns:
            Any | None: The newly created adopter.
        """

    @abstractmethod
    async def update_adopter(
        self,
        adopter_id: int,
        data: AdopterIn,
    ) -> Any | None:
        """The abstract updating adopter data in the data storage.

        Args:
            adopter_id (int): The adopter id.
            data (ContinentIn): The attributes of the adopter.

        Returns:
            Any | None: The updated adopter.
        """

    @abstractmethod
    async def delete_adopter(self, adopter_id: int) -> bool:
        """The abstract removing adopter from the data storage.

        Args:
            adopter_id (int): The adopter id.

        Returns:
            bool: Success of the operation.
        """
