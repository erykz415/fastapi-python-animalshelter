"""A module containing medical record endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from animalshelterapi.container import Container
from animalshelterapi.core.domain.medicalrecord import MedicalRecord, MedicalRecordIn
from animalshelterapi.infrastructure.dto.medicalrecorddto import MedicalRecordDTO
from animalshelterapi.infrastructure.services.imedicalrecord import IMedicalRecordService

router = APIRouter()


@router.post("/create", response_model=MedicalRecord, status_code=201)
@inject
async def create_medical_record(
    medical_record: MedicalRecordIn,
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service])
) -> dict:
    """An endpoint for adding new medical records.

    Args:
        medical_record (MedicalRecordIn): The medical record data.
        service (IMedicalRecordService): The injected service dependency.

    Returns:
        dict: The new medical record attributes.
    """

    new_medical_record = await service.add_medical_record(medical_record)

    return new_medical_record.model_dump() if new_medical_record else {}


@router.get("/all", response_model=Iterable[MedicalRecordDTO], status_code=200)
@inject
async def get_all_medical_records(
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service]),
) -> Iterable:
    """An endpoint for getting all medical records.

    Args:
        service (IMedicalRecordService): The injected service dependency.

    Returns:
        Iterable: The medical record attributes collection.
    """

    medical_records = await service.get_all_medical_records()

    return medical_records


@router.get("/{medical_record_id}", response_model=MedicalRecordDTO, status_code=200)
@inject
async def get_medical_record_by_id(
    medical_record_id: int,
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service]),
) -> dict:
    """An endpoint for getting medical record details by id.

    Args:
        medical_record_id (int): The id of the medical record.
        service (IMedicalRecordService): The injected service dependency.

    Raises:
        HTTPException: 404 if medical record does not exist.

    Returns:
        dict: The requested medical record attributes.
    """

    if medical_record := await service.get_medical_record_by_id(medical_record_id=medical_record_id):
        return medical_record.model_dump()

    raise HTTPException(status_code=404, detail="Medical record not found")


@router.get(
        "/animal/{animal_id}",
        response_model=Iterable[MedicalRecordDTO],
        status_code=200,
)
@inject
async def get_medical_record_by_animal_id(
    animal_id: int,
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service]),
) -> Iterable:
    """An endpoint for getting medical records by animal id.

    Args:
        animal_id (int): The id of the animal.
        service (IMedicalRecordService): The injected service dependency.

    Returns:
        dict: The requested medical records.
    """

    medical_records = await service.get_medical_record_by_animal_id(animal_id)

    return medical_records


@router.put("/{medical_record_id}", response_model=MedicalRecord, status_code=201)
@inject
async def update_medical_record(
    medical_record_id: int,
    updated_medical_record: MedicalRecordIn,
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service]),
) -> dict:
    """An endpoint for updating medical record data.

    Args:
        medical_record_id (int): The id of the medical record.
        updated_medical_record (CountryIn): The updated medical record details.
        service (IMedicalRecordService): The injected service dependency.

    Raises:
        HTTPException: 404 if medical record does not exist.

    Returns:
        dict: The updated medical record data.
    """

    if await service.get_medical_record_by_id(medical_record_id=medical_record_id):
        new_updated_medical_record = await service.update_medical_record(
            medical_record_id=medical_record_id,
            data=updated_medical_record,
        )
        return new_updated_medical_record.model_dump() if new_updated_medical_record else {}

    raise HTTPException(status_code=404, detail="Medical record not found")


@router.delete("/{medical_record_id}", status_code=204)
@inject
async def delete_medical_record(
    medical_record_id: int,
    service: IMedicalRecordService = Depends(Provide[Container.medical_record_service]),
) -> None:
    """An endpoint for deleting medical records.

    Args:
        medical_record_id (int): The id of the medical record.
        service (IMedicalRecordService): The injected service dependency.

    Raises:
        HTTPException: 404 if medical record does not exist.
    """

    if await service.get_medical_record_by_id(medical_record_id=medical_record_id):
        await service.delete_medical_record(medical_record_id)

        return

    raise HTTPException(status_code=404, detail="Medical record not found")
