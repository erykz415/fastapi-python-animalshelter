"""Module containing adoption repository implementation."""

from typing import Iterable

from animalshelterapi.core.repositories.iadoption import IAdoptionRepository
from animalshelterapi.core.domain.adoption import Adoption, AdoptionIn, Adopter
from animalshelterapi.infrastructure.repositories.db import adoptions


class AdoptionMockRepository(IAdoptionRepository):
    """A class representing adoption repository."""

    async def get_all_adoptions(self) -> Iterable[Adoption]:
        """The method getting all adoptions from the data storage.

        Returns:
            Iterable[Adoption]: Adoptions in the data storage.
        """

        return adoptions

    async def get_by_animal_id(self, animal_id: int) -> Iterable[Adoption]:
        """The method getting adoption assigned to particular animal.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Adoption | None: Adoption assigned to an animal.
        """

        return list(filter(lambda x: x.animal_id == animal_id, adoptions))

    async def get_by_adopter_id(self, adopter_id: int) -> Iterable[Adoption]:
        """The method getting adoptions assigned to particular adopter.

        Args:
            adopter_id (int): The id of the adopter.

        Returns:
            Iterable[Adoption]: Adoptions assigned to an adopter.
        """

        return list(filter(lambda x: x.adopter_id == adopter_id, adoptions))

    async def get_by_id(self, adoption_id: int) -> Adoption | None:
        """The method getting adoption by provided id.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            Adoption | None: The adoption details.
        """

        return next((obj for obj in adoptions if obj.id == adoption_id), None)

    async def add_adoption(self, data: AdoptionIn) -> None:
        """The method adding new adoption to the data storage.

        Args:
            data (AdoptionIn): The details of the new adoption.

        Returns:
            Adoption: Full details of the newly added adoption.
        """

        adoptions.append(data)

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

        if adoption_pos := \
                next(filter(lambda x: x.id == adoption_id, adoptions)):
            adoptions[adoption_pos] = data

            return Adoption(id=0, **data.model_dump())

        return None

    async def delete_adoption(self, adoption_id: int) -> bool:
        """The method removing adoption from the data storage.

        Args:
            adoption_id (int): The id of the adoption.

        Returns:
            bool: Success of the operation.
        """

        if adoption_pos := \
                next(filter(lambda x: x.id == adoption_id, adoptions)):
            adoptions.remove(adoption_pos)
            return True

        return False
