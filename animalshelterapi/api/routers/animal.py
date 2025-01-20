"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from animalshelterapi.container import Container
from animalshelterapi.core.domain.animal import Animal, AnimalIn
from animalshelterapi.infrastructure.services.ianimal import IAnimalService

router = APIRouter()


@router.post("/create", response_model=Animal, status_code=201)
@inject
async def create_animal(
    animal: AnimalIn,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> dict:
    """An endpoint for adding new animal.

    Args:
        animal (AnimalIn): The animal data.
        service (IAnimalService): The injected service dependency.

    Returns:
        dict: The new animal attributes.
    """

    new_animal = await service.add_animal(animal)

    return new_animal.model_dump() if new_animal else {}


@router.get("/all", response_model=Iterable[Animal], status_code=200)
@inject
async def get_all_animals(
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting all animals.

    Args:
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_all_animals()

    return animals

@router.get("/name/{name}", response_model=Iterable[Animal], status_code=200)
@inject
async def get_animal_by_name(
    name: str,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting animals with given name.

    Args:
        name(str): The animal name.
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_animal_by_name(name)

    return animals

@router.get("/species/{species}", response_model=Iterable[Animal], status_code=200)
@inject
async def get_animal_by_species(
    species: str,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting animals with given species.

    Args:
        species(str): The animal species.
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_animal_by_species(species)

    return animals

@router.get("/breed/{breed}", response_model=Iterable[Animal], status_code=200)
@inject
async def get_animal_by_breed(
    breed: str,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting animals with given breed.

    Args:
        breed(str): The animal breed.
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_animal_by_breed(breed)

    return animals

@router.get("/gender/{gender}", response_model=Iterable[Animal], status_code=200)
@inject
async def get_animal_by_gender(
    gender: str,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting animals with given gender.

    Args:
        gender(str): The animal gender.
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_animal_by_gender(gender)

    return animals

@router.get("/adoption_status/{adoption_status}", response_model=Iterable[Animal], status_code=200)
@inject
async def get_animal_by_adoption_status(
    adoption_status: str,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> Iterable:
    """An endpoint for getting animals with given adoption status.

    Args:
        adoption_status(str): The animal's adoption status.
        service (IAnimalService): The injected service dependency.

    Returns:
        Iterable: The animal attributes' collection.
    """

    animals = await service.get_animal_by_adoption_status(adoption_status)

    return animals

@router.get("/{animal_id}", response_model=Animal, status_code=200)
@inject
async def get_animal_by_id(
    animal_id: int,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> dict:
    """An endpoint for getting animal details by id.

    Args:
        animal_id (int): The id of the animal.
        service (IAnimalService): The injected service dependency.

    Raises:
        HTTPException: 404 if animal does not exist.

    Returns:
        dict: The requested animal attributes.
    """

    if animal := await service.get_animal_by_id(animal_id):
        return animal.model_dump()

    raise HTTPException(status_code=404, detail="Animal not found")


@router.put("/{animal_id}", response_model=Animal, status_code=201)
@inject
async def update_animal(
    animal_id: int,
    updated_animal: AnimalIn,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> dict:
    """An endpoint for updating animal data.

    Args:
        animal_id (int): The id of the animal.
        updated_animal (AnimalIn): The updated animal details.
        service (IAnimalService): The injected service dependency.

    Raises:
        HTTPException: 404 if animal does not exist.

    Returns:
        dict: The updated animal details.
    """

    if await service.get_animal_by_id(animal_id=animal_id):
        new_updated_animal = await service.update_animal(
            animal_id=animal_id,
            data=updated_animal,
        )
        return new_updated_animal.model_dump() if new_updated_animal \
            else {}

    raise HTTPException(status_code=404, detail="Animal not found")


@router.delete("/{animal_id}", status_code=204)
@inject
async def delete_animal(
    animal_id: int,
    service: IAnimalService = Depends(Provide[Container.animal_service]),
) -> None:
    """An endpoint for deleting animals.

    Args:
        animal_id (int): The id of the animal.
        service (IAnimalService): The injected service dependency.

    Raises:
        HTTPException: 404 if animal does not exist.

    Returns:
        dict: Empty if operation finished.
    """

    if await service.get_animal_by_id(animal_id=animal_id):
        await service.delete_animal(animal_id)
        return

    raise HTTPException(status_code=404, detail="Animal not found")
