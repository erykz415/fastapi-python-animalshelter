"""Module containing animal service implementation."""

from typing import Iterable


from animalshelterapi.core.domain.animal import Animal, AnimalIn
from animalshelterapi.core.repositories.ianimal import IAnimalRepository
from animalshelterapi.infrastructure.services.ianimal import IAnimalService


class AnimalService(IAnimalService):
    """A class implementing the continent service."""

    _repository: IAnimalRepository

    def __init__(self, repository: IAnimalRepository) -> None:
        """The initializer of the `animal service`.

        Args:
            repository (IAnimalRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_animal_by_id(self, animal_id: int) -> Animal | None:
        """The method getting an animal from the repository.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Animal | None: The animal data if exists.
        """

        return await self._repository.get_animal_by_id(animal_id)

    async def get_animal_by_name(self, name: str) -> Iterable[Animal]:
        """The method getting an animal from the repository.

        Args:
            name (str): The name of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return await self._repository.get_animal_by_name(name)

    async def get_animal_by_species(self, species: str) -> Iterable[Animal]:
        """The method getting an animal from the repository.

        Args:
            species (str): The species of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return await self._repository.get_animal_by_species(species)

    async def get_animal_by_breed(self, breed: str) -> Iterable[Animal]:
        """The method getting an animal from the repository.

        Args:
            breed (str): The breed of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return await self._repository.get_animal_by_breed(breed)

    async def get_animal_by_gender(self, gender: str) -> Iterable[Animal]:
        """The method getting an animal from the repository.

        Args:
            gender (str): The gender of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return await self._repository.get_animal_by_gender(gender)

    async def get_animal_by_adoption_status(self, adoption_status: str) -> Iterable[Animal]:
        """The method getting an animal from the repository.

        Args:
            adoption_status (str): The adoption status of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return await self._repository.get_animal_by_adoption_status(adoption_status)

    async def get_all_animals(self) -> Iterable[Animal]:
        """The method getting all animals from the repository.

        Returns:
            Iterable[Animal]: The collection of the all animals.
        """

        return await self._repository.get_all_animals()

    async def add_animal(self, data: AnimalIn) -> Animal | None:
        """The method adding new animal to the repository.

        Args:
            data (AnimalIn): The attributes of the animal.

        Returns:
            Animal | None: The newly created animal.
        """

        return await self._repository.add_animal(data)

    async def update_animal(
        self,
        animal_id: int,
        data: AnimalIn,
    ) -> Animal | None:
        """The method updating animal data in the repository.

        Args:
            animal_id (int): The animal id.
            data (AnimalIn): The attributes of the animal.

        Returns:
            Animal | None: The updated animal.
        """

        return await self._repository.update_animal(
            animal_id=animal_id,
            data=data,
        )

    async def delete_animal(self, animal_id: int) -> bool:
        """The method removing animal from the repository.

        Args:
            animal_id (int): The animal id.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_animal(animal_id)
