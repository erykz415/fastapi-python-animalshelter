"""Module containing animal repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from animalshelterapi.core.domain.animal import AnimalIn


class IAnimalRepository(ABC):
    """An abstract class representing protocol of animal repository."""

    @abstractmethod
    async def get_animal_by_id(self, animal_id: int) -> Any | None:
        """The abstract getting an animal from the data storage.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Any | None: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_name(self, name: str) -> Iterable[Any]:
        """The abstract getting animals from the data storage.

        Args:
            name (str): The name of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_species(self, species: str) -> Iterable[Any]:
        """The abstract getting animals from the data storage.

        Args:
            species (str): The species of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_breed(self, breed: str) -> Iterable[Any]:
        """The abstract getting animals from the data storage.

        Args:
            breed (str): The breed of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_gender(self, gender: str) -> Iterable[Any]:
        """The abstract getting animals from the data storage.

        Args:
            gender (str): The gender of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

    @abstractmethod
    async def get_animal_by_adoption_status(self, adoption_status: str) -> Iterable[Any]:
        """The abstract getting animals from the data storage.

        Args:
             adoption_status (str): The adoption status of the animal.

         Returns:
            Iterable[Any]: The animal data if exists.
        """

    @abstractmethod
    async def get_all_animals(self) -> Iterable[Any]:
        """The abstract getting all animals from the data storage.

        Returns:
            Iterable[Any]: The collection of the all animals.
        """

    @abstractmethod
    async def add_animal(self, data: AnimalIn) -> Any | None:
        """The abstract adding new continent to the data storage.

        Args:
            data (ContinentIn): The attributes of the continent.

        Returns:
            Any | None: The newly created continent.
        """

    @abstractmethod
    async def update_animal(
        self,
        animal_id: int,
        data: AnimalIn,
    ) -> Any | None:
        """The abstract updating animal data in the data storage.

        Args:
            animal_id (int): The animal id.
            data (AnimalIn): The attributes of the animal.

        Returns:
            Any | None: The updated animal.
        """

    @abstractmethod
    async def delete_animal(self, animal_id: int) -> bool:
        """The abstract updating removing animal from the data storage.

        Args:
            animal_id (int): The animal id.

        Returns:
            bool: Success of the operation.
        """
