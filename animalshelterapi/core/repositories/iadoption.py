"""Module containing adoption repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from animalshelterapi.core.domain.adoption import AdoptionIn


class IAdoptionRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_adoptions(self) -> Iterable[Any]:
        """The abstract getting all adoptions from the data storage.

        Returns:
            Iterable[Any]: Adoptions in the data storage.
        """

    @abstractmethod
    async def get_by_animal_id(self, animal_id: int) -> Iterable[Any]:
        """The abstract getting adoptions assigned to particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[Any]: Adoptions assigned to an animal.
        """

    @abstractmethod
    async def get_by_adopter_id(self, adopter_id: int) -> Iterable[Any]:
        """The abstract getting adoptions assigned to particular adopter.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Iterable[Any]: Adoptions assigned to an adopter.
        """

    @abstractmethod
    async def get_by_id(self, adoption_id: int) -> Any | None:
        """The abstract getting adoption by provided id.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            Any | None: The adoption details.
        """

    @abstractmethod
    async def add_adoption(self, data: AdoptionIn) -> Any | None:
        """The abstract adding new adoption to the data storage.

        Args:
            data (AdoptionIn): The details of the new adoption.

        Returns:
            Any | None: The newly added adoption.
        """

    @abstractmethod
    async def update_adoption(
        self,
        adoption_id: int,
        data: AdoptionIn,
    ) -> Any | None:
        """The abstract updating adoption data in the data storage.

        Args:
            adoption_id (int): The id of the adoption.
            data (AdoptionIn): The details of the updated adoption.

        Returns:
            Any | None: The updated adoption details.
        """

    @abstractmethod
    async def delete_adoption(self, adoption_id: int) -> bool:
        """The abstract updating removing adoption from the data storage.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            bool: Success of the operation.
        """
