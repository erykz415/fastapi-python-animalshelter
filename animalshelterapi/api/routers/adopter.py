"""A module containing adopter endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from animalshelterapi.container import Container
from animalshelterapi.core.domain.adoption import Adopter, AdopterIn
from animalshelterapi.infrastructure.services.iadopter import IAdopterService

router = APIRouter()


@router.post("/create", response_model=Adopter, status_code=201)
@inject
async def create_adopter(
    adopter: AdopterIn,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> dict:
    """An endpoint for adding new adopter.

    Args:
        adopter (AdopterIn): The adopter data.
        service (IAdopterService): The injected service dependency.

    Returns:
        dict: The new adopter attributes.
    """

    new_adopter = await service.add_adopter(adopter)

    return new_adopter.model_dump() if new_adopter else {}


@router.get("/all", response_model=Iterable[Adopter], status_code=200)
@inject
async def get_all_adopters(
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> Iterable:
    """An endpoint for getting all adopters.

    Args:
        service (IAdopterService): The injected service dependency.

    Returns:
        Iterable: The adopter attributes collection.
    """

    adopters = await service.get_all_adopters()

    return adopters


@router.get("/last_name/{last_name}", response_model=Iterable[Adopter], status_code=200)
@inject
async def get_adopter_by_last_name(
    last_name: str,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> Iterable:
    """An endpoint for getting adopters by last name.

    Args:
        last_name (int): The last name of the adopter.
        service (IAdopterService): The injected service dependency.

    Returns:
        Iterable: The adopter attributes' collection
    """

    adopters = await service.get_adopter_by_last_name(last_name)

    return adopters

@router.get("/phone_number/{phone_number}", response_model=Iterable[Adopter], status_code=200)
@inject
async def get_adopter_by_phone_number(
    phone_number: str,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> Iterable:
    """An endpoint for getting adopters by phone number.

    Args:
        phone_number (str): The phone number of the adopter.
        service (IAdopterService): The injected service dependency.

    Returns:
        Iterable: The adopter attributes' collection
    """

    adopters = await service.get_adopter_by_phone_number(phone_number)

    return adopters


@router.get("/{adopter_id}", response_model=Adopter, status_code=200)
@inject
async def get_adopter_by_id(
    adopter_id: int,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> dict:
    """An endpoint for getting adopter details by id.

    Args:
        adopter_id (int): The id of the adopter.
        service (IAdopterService): The injected service dependency.

    Raises:
        HTTPException: 404 if adopter does not exist.

    Returns:
        dict: The requested adopter attributes.
    """

    if adopter := await service.get_adopter_by_id(adopter_id):
        return adopter.model_dump()

    raise HTTPException(status_code=404, detail="Adopter not found")


@router.put("/{adopter_id}", response_model=Adopter, status_code=201)
@inject
async def update_adopter(
    adopter_id: int,
    updated_adopter: AdopterIn,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> dict:
    """An endpoint for updating adopter data.

    Args:
        adopter_id (int): The id of the adopter.
        updated_adopter (AdopterIn): The updated adopter details.
        service (IAdopterService): The injected service dependency.

    Raises:
        HTTPException: 404 if adopter does not exist.

    Returns:
        dict: The updated adopter details.
    """

    if await service.get_adopter_by_id(adopter_id=adopter_id):
        new_updated_adopter = await service.update_adopter(
            adopter_id=adopter_id,
            data=updated_adopter,
        )
        return new_updated_adopter.model_dump() if new_updated_adopter \
            else {}

    raise HTTPException(status_code=404, detail="Adopter not found")


@router.delete("/{adopter_id}", status_code=204)
@inject
async def delete_adopter(
    adopter_id: int,
    service: IAdopterService = Depends(Provide[Container.adopter_service]),
) -> None:
    """An endpoint for deleting adopters.

    Args:
        adopter_id (int): The id of the adopter.
        service (IAdopterService): The injected service dependency.

    Raises:
        HTTPException: 404 if adopter does not exist.

    Returns:
        dict: Empty if operation finished.
    """

    if await service.get_adopter_by_id(adopter_id=adopter_id):
        await service.delete_adopter(adopter_id)
        return

    raise HTTPException(status_code=404, detail="Adopter not found")
