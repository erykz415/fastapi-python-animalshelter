"""Module containing report service implementation."""

from typing import Iterable


from animalshelterapi.core.repositories.ireport import IReportRepository
from animalshelterapi.infrastructure.dto.reportdto import ReportDTO
from animalshelterapi.infrastructure.services.ireport import IReportService


class ReportService(IReportService):
    """A class implementing the continent service."""

    _repository: IReportRepository

    def __init__(self, repository: IReportRepository):
        """Initialize the report service with the repository."""
        self._repository = repository

    async def get_animals_report(self) -> Iterable[ReportDTO]:
        """The method getting report from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

        return await self._repository.get_animals_report()

    async def get_medical_records_report(self) -> Iterable[ReportDTO]:
        """The method getting report from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

        return await self._repository.get_medical_records_report()

    async def get_adoptions_report(self) -> Iterable[ReportDTO]:
        """The method getting report from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

        return await self._repository.get_adoptions_report()

