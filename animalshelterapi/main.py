"""Main module of the app"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from animalshelterapi.api.routers.animal import router as animal_router
from animalshelterapi.api.routers.adopter import router as adopter_router
from animalshelterapi.api.routers.adoption import router as adoption_router
from animalshelterapi.api.routers.medicalrecord import router as medical_record_router
from animalshelterapi.api.routers.report import router as report_router
from animalshelterapi.container import Container
from animalshelterapi.db import database
from animalshelterapi.db import init_db

container = Container()
container.wire(modules=[
    "animalshelterapi.api.routers.animal",
    "animalshelterapi.api.routers.adopter",
    "animalshelterapi.api.routers.adoption",
    "animalshelterapi.api.routers.medicalrecord",
    "animalshelterapi.api.routers.report",
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(animal_router, prefix="/animal")
app.include_router(adopter_router, prefix="/adopter")
app.include_router(adoption_router, prefix="/adoption")
app.include_router(medical_record_router, prefix="/medicalrecord")
app.include_router(report_router, prefix="/report")



@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:
    """A function handling http exceptions for logging purposes.

    Args:
        request (Request): The incoming HTTP request.
        exception (HTTPException): A related exception.

    Returns:
        Response: The HTTP response.
    """
    return await http_exception_handler(request, exception)
