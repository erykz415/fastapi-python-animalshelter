"""Module containing animal repository implementation."""

from typing import Iterable

from animalshelterapi.core.domain.animal import Animal, AnimalIn
from animalshelterapi.core.repositories.ianimal import IAnimalRepository
from animalshelterapi.infrastructure.repositories.db import animals


class AnimalRepository(IAnimalRepository):
    """A class implementing the animal repository."""

    async def get_animal_by_id(self, animal_id: int) -> Animal | None:
        """The method getting an animal from the data storage.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Animal | None: The animal data if exists.
        """

        return next(
            (obj for obj in animals if obj.id == animal_id),
            None,
        )

    async def get_animal_by_name(self, name: str) -> Iterable[Animal]:
        """The method getting animals from the data storage.

        Args:
            name (str): The name of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return (obj for obj in animals if obj.name == name)

    async def get_animal_by_species(self, species: str) -> Iterable[Animal]:
        """The method getting animals from the data storage.

        Args:
            species (str): The species of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return (obj for obj in animals if obj.species == species)

    async def get_animal_by_breed(self, breed: str) -> Iterable[Animal]:
        """The method getting animals from the data storage.

        Args:
            breed (str): The breed of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return (obj for obj in animals if obj.breed == breed)

    async def get_animal_by_gender(self, gender: str) -> Iterable[Animal]:
        """The method getting animals from the data storage.

        Args:
            gender (str): The gender of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return (obj for obj in animals if obj.gender == gender)

    async def get_animal_by_adoption_status(self, adoption_status: str) -> Iterable[Animal]:
        """The method getting animals from the data storage.

        Args:
            adoption_status (str): The adoption status of the animal.

        Returns:
            Iterable[Animal]: The animal data if exists.
        """

        return (obj for obj in animals if obj.adoption_status == adoption_status)

    async def get_all_animals(self) -> Iterable[Animal]:
        """The method getting all animals from the data storage.

        Returns:
            Iterable[Animal]: The collection of the all animals.
        """

        return animals

    async def add_animal(self, data: AnimalIn) -> None:
        """The method adding new animal to the data storage.

        Args:
            data (AnimalIn): The attributes of the animal.
        """

        animals.append(data)

    async def update_animal(
        self,
        animal_id: int,
        data: AnimalIn,
    ) -> Animal | None:
        """The method updating animal data in the data storage.

        Args:
            animal_id (int): The animal id.
            data (AnimalIn): The attributes of the animal.

        Returns:
            Animal | None: The updated animal.
        """

        if animal_pos := \
                next(filter(lambda x: x.id == animal_id, animals)):
            animals[animal_pos] = data

            return Animal(id=0, **data.model_dump())

        return None

    async def delete_animal(self, animal_id: int) -> bool:
        """The method removing animal from the data storage.

        Args:
            animal_id (int): The animal id.

        Returns:
            bool: Success of the operation.
        """

        if animal_pos := \
                next(filter(lambda x: x.id == animal_id, animals)):
            animals.remove(animal_pos)
            return True

        return False
