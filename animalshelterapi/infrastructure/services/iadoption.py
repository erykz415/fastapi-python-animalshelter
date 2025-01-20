"""Module containing adoption service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from animalshelterapi.core.domain.adoption import Adoption, AdoptionIn
from animalshelterapi.infrastructure.dto.adoptiondto import AdoptionDTO


class IAdoptionService(ABC):
    """A class representing airport repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[AdoptionDTO]:
        """The method getting all adoptions from the repository.

        Returns:
            Iterable[AdoptionDTO]: All adoptions.
        """

    @abstractmethod
    async def get_by_animal_id(self, animal_id: int) -> Iterable[Adoption]:
        """The method getting adoption assigned to particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[Adoption]: The adoption details.
        """

    @abstractmethod
    async def get_by_adopter_id(self, adopter_id: int) -> Iterable[Adoption]:
        """The method getting adoptions assigned to particular adopter.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Iterable[Adoption]: Adoptions assigned to an adopter.
        """

    @abstractmethod
    async def get_by_id(self, adoption_id: int) -> AdoptionDTO | None:
        """The method getting adoption by provided id.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            AdoptionDTO | None: The adoption details.
        """

    @abstractmethod
    async def add_adoption(self, data: AdoptionIn) -> Adoption | None:
        """The method adding new adoption to the data storage.

        Args:
            data (AdoptionIn): The details of the new adoption.

        Returns:
            Adoption | None: Full details of the newly added adoption.
        """

    @abstractmethod
    async def update_adoption(
        self,
        adoption_id: int,
        data: AdoptionIn,
    ) -> Adoption | None:
        """The method updating adoption data in the data storage.

        Args:
            adoption_id (int): The id of the adoption.
            data (AdoptionIn): The details of the updated adoption.

        Returns:
            Adoption | None: The updated adoption details.
        """

    @abstractmethod
    async def delete_adoption(self, adoption_id: int) -> bool:
        """The method removing adoption from the data storage.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            bool: Success of the operation.
        """
