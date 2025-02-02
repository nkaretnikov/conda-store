from fastapi import Request, Depends
from sqlalchemy.orm import Session


async def get_conda_store(request: Request):
    return request.state.conda_store


async def get_server(request: Request):
    return request.state.server


async def get_auth(request: Request):
    return request.state.authentication


async def get_entity(request: Request, auth=Depends(get_auth)):
    return auth.authenticate_request(request)


async def get_templates(request: Request):
    return request.state.templates


async def get_db(request: Request, conda_store=Depends(get_conda_store)) -> Session:
    db = conda_store.session_factory()
    try:
        yield db
    finally:
        db.close()
