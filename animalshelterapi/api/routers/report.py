"""A module containing report endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


from animalshelterapi.container import Container
from animalshelterapi.core.domain.report import Report, ReportIn
from animalshelterapi.infrastructure.dto.reportdto import ReportDTO
from animalshelterapi.infrastructure.services.ireport import IReportService


bearer_scheme = HTTPBearer()

router = APIRouter()
@router.get("/adoption_report/{adoptions_report}", response_model=None, status_code=200)
@inject
async def get_adoptions_report(
    service: IReportService = Depends(Provide[Container.report_service]),
) -> Iterable:
    """An endpoint for getting adoptions report.

    Args:
        service (IReportService): The injected service dependency.

    Returns:
        Iterable: The report attributes collection.
    """

    report = await service.get_adoptions_report()

    return report

@router.get("/medical_records_report/{medical_records_report}", response_model=None, status_code=200)
@inject
async def get_medical_records_report(
    service: IReportService = Depends(Provide[Container.report_service]),
) -> Iterable:
    """An endpoint for getting medical records report.

    Args:
        service (IReportService): The injected service dependency.

    Returns:
        Iterable: The report attributes collection.
    """

    report = await service.get_medical_records_report()

    return report

@router.get("/animals_report/{animals_report}", response_model=None, status_code=200)
@inject
async def get_animals_report(
    service: IReportService = Depends(Provide[Container.report_service]),
) -> Iterable:
    """An endpoint for getting report.

    Args:
        service (IReportService): The injected service dependency.

    Returns:
        Iterable: The report attributes collection.
    """

    report = await service.get_animals_report()

    return report

