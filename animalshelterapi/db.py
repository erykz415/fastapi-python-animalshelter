"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (    # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from animalshelterapi.config import config

metadata = sqlalchemy.MetaData()

animal_table = sqlalchemy.Table(
    "animals",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("species", sqlalchemy.String),
    sqlalchemy.Column("breed", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("gender", sqlalchemy.String),
    sqlalchemy.Column("arrival_date", sqlalchemy.Date),
    sqlalchemy.Column("adoption_status", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
)

adopter_table = sqlalchemy.Table(
    "adopters",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("address", sqlalchemy.String),
)

adoption_table = sqlalchemy.Table(
    "adoptions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "animal_id",
        sqlalchemy.ForeignKey("animals.id"),
        nullable=False,
    ),
    sqlalchemy.Column(
        "adopter_id",
        sqlalchemy.ForeignKey("adopters.id"),
        nullable=False,
    ),
    sqlalchemy.Column("adoption_date", sqlalchemy.Date),
)

medical_record_table = sqlalchemy.Table(
    "medical_records",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "animal_id",
        sqlalchemy.ForeignKey("animals.id"),
        nullable=False,
    ),
    sqlalchemy.Column("visit_date", sqlalchemy.Date),
    sqlalchemy.Column("diagnosis", sqlalchemy.String),
    sqlalchemy.Column("treatment", sqlalchemy.String, nullable=True),
)

db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    #force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            return
        except (
            OperationalError,
            DatabaseError,
            CannotConnectNowError,
            ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")
