"""Module containing continent service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from animalshelterapi.infrastructure.dto.reportdto import ReportDTO


class IReportService(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_adoptions_report(self) -> Iterable[ReportDTO]:
        """The method getting reports from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

    @abstractmethod
    async def get_medical_records_report(self) -> Iterable[ReportDTO]:
        """The method getting reports from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

    @abstractmethod
    async def get_animals_report(self) -> Iterable[ReportDTO]:
        """The method getting reports from the repository.

        Returns:
            Iterable[ReportDTO]: report.
        """

