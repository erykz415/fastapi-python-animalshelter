from datetime import datetime, timedelta
from sqlalchemy import select, func
from animalshelterapi.core.repositories.ireport import IReportRepository
from animalshelterapi.db import (
    adoption_table,
    medical_record_table,
    animal_table,
    database,
)
from animalshelterapi.infrastructure.dto.reportdto import ReportDTO


class ReportRepository(IReportRepository):
    """A class representing report DB repository."""

    async def get_adoptions_report(self) -> ReportDTO:
        """The method generating a report about number of adoptions
        in the last day, week, and month."""

        now = datetime.now()
        last_day = now - timedelta(days=1)
        last_week = now - timedelta(days=7)
        last_month = now - timedelta(days=30)

        print(last_day)
        print(last_week)
        print(last_month)

        query_day = select(func.count()).where(adoption_table.c.adoption_date >= last_day)
        query_week = select(func.count()).where(adoption_table.c.adoption_date >= last_week)
        query_month = select(func.count()).where(adoption_table.c.adoption_date >= last_month)

        day_count = await database.fetch_val(query_day)
        week_count = await database.fetch_val(query_week)
        month_count = await database.fetch_val(query_month)

        fake_record = {
            "topic": "Adoptions Report",
            "content": (
                f"adoptions_last_day: {day_count}, "
                f"adoptions_last_week: {week_count}, "
                f"adoptions_last_month: {month_count}"
            ),
        }

        # fake_obj_record = Report(**dict(fake_record))

        return ReportDTO.from_record(fake_record)

    async def get_medical_records_report(self) -> ReportDTO:
        """The method generating a report about the number of medical records
        in the last day, week, and month."""

        now = datetime.now()
        last_day = now - timedelta(days=1)
        last_week = now - timedelta(days=7)
        last_month = now - timedelta(days=30)

        print(last_day)
        print(last_week)
        print(last_month)

        query_day = select(func.count()).where(medical_record_table.c.visit_date >= last_day)
        query_week = select(func.count()).where(medical_record_table.c.visit_date >= last_week)
        query_month = select(func.count()).where(medical_record_table.c.visit_date >= last_month)

        day_count = await database.fetch_val(query_day)
        week_count = await database.fetch_val(query_week)
        month_count = await database.fetch_val(query_month)

        fake_record = {
            "topic": "Medical records Report",
            "content": (
                f"medical_records_last_day: {day_count}, "
                f"medical_records_last_week: {week_count}, "
                f"medical_records_last_month: {month_count}"
            ),
        }


        return ReportDTO.from_record(fake_record)

    async def get_animals_report(self) -> ReportDTO:
        """The method generating a report about the number of animals
        in the shelter in the last day, week, and month."""

        now = datetime.now()
        last_day = now - timedelta(days=1)
        last_week = now - timedelta(days=7)
        last_month = now - timedelta(days=30)

        print(last_day)
        print(last_week)
        print(last_month)

        query_day = select(func.count()).where(animal_table.c.arrival_date >= last_day)
        query_week = select(func.count()).where(animal_table.c.arrival_date >= last_week)
        query_month = select(func.count()).where(animal_table.c.arrival_date >= last_month)

        day_count = await database.fetch_val(query_day)
        week_count = await database.fetch_val(query_week)
        month_count = await database.fetch_val(query_month)

        fake_record = {
            "topic": "Animals in shelter Report",
            "content": (
                f"animals_last_day: {day_count}, "
                f"animals_last_week: {week_count}, "
                f"animals_last_month: {month_count}"
            ),
        }

        return ReportDTO.from_record(fake_record)
