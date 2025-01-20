"""Module containing animal repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from animalshelterapi.core.domain.animal import AnimalIn


class IReportRepository(ABC):
    """An abstract class representing protocol of animal repository."""

    @abstractmethod
    async def get_adoptions_report(self) -> Iterable[Any]:
        """The abstract getting a report about number
         of adoptions from the data storage.

        Returns:
            Iterable[Any]: Report
        """

    @abstractmethod
    async def get_medical_records_report(self) -> Iterable[Any]:
        """The abstract getting a report about number
         of medical reports from the data storage.

        Returns:
            Iterable[Any]: Report
        """

    @abstractmethod
    async def get_animals_report(self) -> Iterable[Any]:
        """The abstract getting a report about number
         of animals in shelter from the data storage.

        Returns:
            Iterable[Any]: Report
        """

