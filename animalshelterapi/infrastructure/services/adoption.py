
"""Module containing continent service implementation."""

from typing import Iterable

from animalshelterapi.core.domain.adoption import Adoption, AdoptionIn
from animalshelterapi.core.repositories.iadoption import IAdoptionRepository
from animalshelterapi.infrastructure.dto.adoptiondto import AdoptionDTO
from animalshelterapi.infrastructure.services.iadoption import IAdoptionService


class AdoptionService(IAdoptionService):
    """A class implementing the airport service."""

    _repository: IAdoptionRepository

    def __init__(self, repository: IAdoptionRepository) -> None:
        """The initializer of the `adoption service`.

        Args:
            repository (IAdoptionRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all(self) -> Iterable[AdoptionDTO]:
        """The method getting all adoptions from the repository.

        Returns:
            Iterable[AdoptionDTO]: All adoptions.
        """

        return await self._repository.get_all_adoptions()

    async def get_by_animal_id(self, animal_id: int) -> Iterable[Adoption]:
        """The method getting adoption assigned to particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Iterable[Adoption]: The adoption details
        """

        return await self._repository.get_by_animal_id(animal_id)

    async def get_by_adopter_id(self, adopter_id: int) -> Iterable[Adoption]:
        """The method getting adoptions assigned to particular adopter.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Iterable[Adoption]: Adoptions assigned to an adopter.
        """

        return await self._repository.get_by_adopter_id(adopter_id)

    async def get_by_id(self, adoption_id: int) -> AdoptionDTO | None:
        """The method getting adoption by provided id.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            AdoptionDTO | None: The adoption details.
        """

        return await self._repository.get_by_id(adoption_id)

    async def add_adoption(self, data: AdoptionIn) -> Adoption | None:
        """The method adding new adoption to the data storage.

        Args:
            data (AdoptionIn): The details of the new adoption.

        Returns:
            Adoption | None: Full details of the newly added adoption.
        """

        return await self._repository.add_adoption(data)

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

        return await self._repository.update_adoption(
            adoption_id=adoption_id,
            data=data,
        )

    async def delete_adoption(self, adoption_id: int) -> bool:
        """The method removing adoption from the data storage.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_adoption(adoption_id)
