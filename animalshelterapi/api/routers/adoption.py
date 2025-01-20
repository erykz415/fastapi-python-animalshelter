
"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from animalshelterapi.container import Container
from animalshelterapi.core.domain.adoption import Adoption, AdoptionIn
from animalshelterapi.infrastructure.dto.adoptiondto import AdoptionDTO
from animalshelterapi.infrastructure.services.iadoption import IAdoptionService

router = APIRouter()


@router.post("/create", response_model=Adoption, status_code=201)
@inject
async def create_adoption(
    adoption: AdoptionIn,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> dict:
    """An endpoint for adding new adoption.

    Args:
        adoption (AdoptionIn): The adoption data.
        service (IAdoptionService): The injected service dependency.

    Returns:
        dict: The new adoption attributes.
    """

    new_adoption = await service.add_adoption(adoption)

    return new_adoption.model_dump() if new_adoption else {}


@router.get("/all", response_model=Iterable[AdoptionDTO], status_code=200)
@inject
async def get_all_adoptions(
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> Iterable:
    """An endpoint for getting all adoptions.

    Args:
        service (IAdoptionService): The injected service dependency.

    Returns:
        Iterable: The adoption attributes collection.
    """

    adoptions = await service.get_all()

    return adoptions


@router.get(
        "/animal/{animal_id}",
        response_model=Iterable[Adoption],
        status_code=200,
)
@inject
async def get_adoption_by_animal_id(
    animal_id: int,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> Iterable:
    """An endpoint for getting adoption by animal id.

    Args:
        animal_id (int): The id of the animal.
        service (IAdoptionService): The injected service dependency.

    Returns:
        Iterable: The adoption details.
    """

    adoptions = await service.get_by_animal_id(animal_id)

    return adoptions


@router.get(
        "/adopter/{adopter_id}",
        response_model=Iterable[Adoption],
        status_code=200,
)
@inject
async def get_adoption_by_adopter_id(
    adopter_id: int,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> Iterable:
    """An endpoint for getting adoptions by adopter id.

    Args:
        adopter_id (int): The id of the adopter.
        service (IAdoptionService): The injected service dependency.

    Returns:
        Iterable: The adoption details collection.
    """

    adoptions = await service.get_by_adopter_id(adopter_id)

    return adoptions


@router.get(
        "/{adoption_id}",
        response_model=AdoptionDTO,
        status_code=200,
)
@inject
async def get_adoption_by_id(
    adoption_id: int,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> dict | None:
    """An endpoint for getting adoption by id.

    Args:
        adoption_id (int): The id of the adoption.
        service (IAdoptionService): The injected service dependency.

    Returns:
        dict | None: The adoption details.
    """

    if adoption := await service.get_by_id(adoption_id):
        return adoption.model_dump()

    raise HTTPException(status_code=404, detail="Adoption not found")


@router.put("/{adoption_id}", response_model=Adoption, status_code=201)
@inject
async def update_adoption(
    adoption_id: int,
    updated_adoption: AdoptionIn,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> dict:
    """An endpoint for updating adoption data.

    Args:
        adoption_id (int): The id of the adoption.
        updated_adoption (AdoptionIn): The updated adoption details.
        service (IAdoptionService): The injected service dependency.

    Raises:
        HTTPException: 404 if adoption does not exist.

    Returns:
        dict: The updated adoption details.
    """

    if await service.get_by_id(adoption_id=adoption_id):
        await service.update_adoption(
            adoption_id=adoption_id,
            data=updated_adoption,
        )
        return {**updated_adoption.model_dump(), "id": adoption_id}

    raise HTTPException(status_code=404, detail="Adoption not found")


@router.delete("/{adoption_id}", status_code=204)
@inject
async def delete_adoption(
    adoption_id: int,
    service: IAdoptionService = Depends(Provide[Container.adoption_service]),
) -> None:
    """An endpoint for deleting adoptions.

    Args:
        adoption_id (int): The id of the adoption.
        service (IAdoptionService): The injected service dependency.

    Raises:
        HTTPException: 404 if adoption does not exist.
    """

    if await service.get_by_id(adoption_id=adoption_id):
        await service.delete_adoption(adoption_id)

        return

    raise HTTPException(status_code=404, detail="Adoption not found")
