"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from animalshelterapi.infrastructure.repositories.animaldb import \
    AnimalRepository
from animalshelterapi.infrastructure.repositories.adopterdb import \
    AdopterRepository
from animalshelterapi.infrastructure.repositories.adoptiondb import \
    AdoptionRepository
from animalshelterapi.infrastructure.repositories.medicalrecorddb import \
    MedicalRecordRepository
from animalshelterapi.infrastructure.repositories.reportdb import ReportRepository
from animalshelterapi.infrastructure.services.adopter import AdopterService
from animalshelterapi.infrastructure.services.adoption import AdoptionService
from animalshelterapi.infrastructure.services.animal import AnimalService
from animalshelterapi.infrastructure.services.medicalrecord import MedicalRecordService
from animalshelterapi.infrastructure.services.report import ReportService


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    animal_repository = Singleton(AnimalRepository)
    adopter_repository = Singleton(AdopterRepository)
    adoption_repository = Singleton(AdoptionRepository)
    medical_record_repository = Singleton(MedicalRecordRepository)
    report_repository = Singleton(ReportRepository)

    animal_service = Factory(
        AnimalService,
        repository=animal_repository,
    )

    adopter_service = Factory(
        AdopterService,
        repository=adopter_repository,
    )

    adoption_service = Factory(
        AdoptionService,
        repository=adoption_repository,
    )

    medical_record_service = Factory(
        MedicalRecordService,
        repository=medical_record_repository,
    )

    report_service = Factory(
        ReportService,
        repository=report_repository,
    )


