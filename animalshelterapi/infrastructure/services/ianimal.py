"""Module containing continent service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from animalshelterapi.core.domain.animal import Animal, AnimalIn


class IAnimalService(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_animal_by_id(self, animal_id: int) -> Animal | None:
        """The abstract getting an animal from the repository.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Animal | None: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_name(self, name: str) -> Iterable[Animal]:
        """The abstract getting animals from the repository.

        Args:
            name (str): The name of the animal.

        Returns:
            Iterable[Animal]: The collection of all animals with given name.
        """

    @abstractmethod
    async def get_animal_by_species(self, species: str) -> Iterable[Animal]:
        """The abstract getting animals from the repository.

        Args:
            species (str): The species of the animal.

        Returns:
            Iterable[Animal]: The collection of all animals with given species.
        """

    @abstractmethod
    async def get_animal_by_breed(self, breed: str) -> Iterable[Animal]:
        """The abstract getting animals from the repository.

        Args:
            breed (str): The breed of the animal.

        Returns:
            Iterable[Animal]: The collection of all animals with given breed.
        """

    @abstractmethod
    async def get_animal_by_gender(self, gender: str) -> Iterable[Animal]:
        """The abstract getting animals from the repository.

        Args:
            gender (str): The gender of the animal.

        Returns:
            Iterable[Animal]: The collection of all animals with given gender.
        """

    @abstractmethod
    async def get_animal_by_adoption_status(self, adoption_status: str) -> Iterable[Animal]:
        """The abstract getting animals from the repository.

        Args:
            adoption_status (str): The adoption status of the animal.

        Returns:
            Iterable[Animal]: The collection of all animals with given adoption status.
        """

    @abstractmethod
    async def get_all_animals(self) -> Iterable[Animal]:
        """The abstract getting all animals from the repository.

        Returns:
            Iterable[Animal]: The collection of the all animals.
        """

    @abstractmethod
    async def add_animal(self, data: AnimalIn) -> Animal | None:
        """The abstract adding new animal to the repository.

        Args:
            data (AnimalIn): The attributes of the animal.

        Returns:
            Animal | None: The newly created animal.
        """

    @abstractmethod
    async def update_animal(
        self,
        animal_id: int,
        data: AnimalIn,
    ) -> Animal | None:
        """The abstract updating animal data in the repository.

        Args:
            animal_id (int): The animal id.
            data (AnimalIn): The attributes of the animal.

        Returns:
            Animal | None: The updated animal.
        """

    @abstractmethod
    async def delete_animal(self, animal_id: int) -> bool:
        """The abstract removing animal from the repository.

        Args:
            animal_id (int): The animal id.

        Returns:
            bool: Success of the operation.
        """
