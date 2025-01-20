"""Module containing continent database repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from animalshelterapi.core.domain.animal import Animal, AnimalIn
from animalshelterapi.core.repositories.ianimal import IAnimalRepository
from animalshelterapi.db import animal_table, database


class AnimalRepository(IAnimalRepository):
    """A class implementing the animal repository."""

    async def get_animal_by_id(self, animal_id: int) -> Any | None:
        """The method getting an animal from the data storage.

        Args:
            animal_id (int): The id of the animal.

        Returns:
            Any | None: The animal data if exists.
        """

        animal = await self._get_by_id(animal_id)

        return Animal(**dict(animal)) if animal else None

    async def get_animal_by_name(self, name: str) -> Iterable[Any]:
        """The method getting animals from the data storage.

        Args:
            name (str): The name of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

        query = animal_table.select().where(animal_table.c.name == name).order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return[Animal(**dict(animal)) for animal in animals]

    async def get_animal_by_species(self, species: str) -> Iterable[Any]:
        """The method getting animals from the data storage.

        Args:
            species (str): The species of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

        query = animal_table.select().where(animal_table.c.species == species).order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return[Animal(**dict(animal)) for animal in animals]

    async def get_animal_by_breed(self, breed: str) -> Iterable[Any]:
        """The method getting animals from the data storage.

        Args:
            breed (str): The breed of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

        query = animal_table.select().where(animal_table.c.breed == breed).order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return[Animal(**dict(animal)) for animal in animals]

    async def get_animal_by_gender(self, gender: str) -> Iterable[Any]:
        """The method getting animals from the data storage.

        Args:
            gender (str): The gender of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

        query = animal_table.select().where(animal_table.c.gender == gender).order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return[Animal(**dict(animal)) for animal in animals]

    async def get_animal_by_adoption_status(self, adoption_status: str) -> Iterable[Any]:
        """The method getting animals from the data storage.

        Args:
            adoption_status (str): The adoption status of the animal.

        Returns:
            Iterable[Any]: The animal data if exists.
        """

        query = animal_table.select().where(animal_table.c.adoption_status == adoption_status).order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return[Animal(**dict(animal)) for animal in animals]

    async def get_all_animals(self) -> Iterable[Any]:
        """The method getting all animals from the data storage.

        Returns:
            Iterable[Any]: The collection of the all animals.
        """

        query = animal_table.select().order_by(animal_table.c.id.asc())
        animals = await database.fetch_all(query)

        return [Animal(**dict(animal)) for animal in animals]

    async def add_animal(self, data: AnimalIn) -> Any | None:
        """The method adding new animal to the data storage.

        Args:
            data (AnimalIn): The attributes of the animal.

        Returns:
            Any | None: The newly created animal.
        """

        query = animal_table.insert().values(**data.model_dump())
        new_animal_id = await database.execute(query)
        new_animal = await self._get_by_id(new_animal_id)

        return Animal(**dict(new_animal)) if new_animal else None

    async def update_animal(
        self,
        animal_id: int,
        data: AnimalIn,
    ) -> Any | None:
        """The method updating animal data in the data storage.

        Args:
            animal_id (int): The animal id.
            data (AnimalIn): The attributes of the animal.

        Returns:
            Any | None: The updated animal.
        """

        if self._get_by_id(animal_id):
            query = (
                animal_table.update()
                .where(animal_table.c.id == animal_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            animal = await self._get_by_id(animal_id)

            return Animal(**dict(animal)) if animal else None

        return None

    async def delete_animal(self, animal_id: int) -> bool:
        """The method removing animal from the data storage.

        Args:
            animal_id (int): The animal id.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(animal_id):
            query = animal_table \
                .delete() \
                .where(animal_table.c.id == animal_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, animal_id: int) -> Record | None:
        """A private method getting animal from the DB based on its ID.

        Args:
            animal_id (int): The ID of the animal.

        Returns:
            Any | None: Animal record if exists.
        """

        query = (
            animal_table.select()
            .where(animal_table.c.id == animal_id)
            .order_by(animal_table.c.id.asc())
        )

        return await database.fetch_one(query)
