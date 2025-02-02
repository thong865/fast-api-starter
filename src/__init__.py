from fastapi import FastAPI

from .errors import register_all_errors
from .middleware import register_middleware
from src.welcome.routes import welcome_router
version = "v1"
description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Start App API",
    description=description,
    version=version,
    license_info={"name":"MIT License","url":"https://opensource.org/license/mit"},
    contact={"name":"","url":"","email":""},
    terms_of_service="",
    openapi_prefix=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)
register_middleware(app)


app.include_router(welcome_router)