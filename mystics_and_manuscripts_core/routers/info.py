from fastapi import APIRouter, HTTPException

from mystics_and_manuscripts_core.internal.version import read_current_version, parse_version, is_version_supported

info_router = APIRouter()


@info_router.get("/")
def info_route() -> dict:
    return {"service": "Mystics and Manuscripts CORE", "version": read_current_version()}


@info_router.get("/is-version-supported/{version}")
def is_version_supported_route(version: str) -> dict:
    # parse the version given by the caller
    # forward the error if the version format is deemed incorrect
    try:
        checked_version = parse_version(version)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # note: its supposed that the core version is always formatted properly
    target_version = parse_version(read_current_version())

    return {"supported": is_version_supported(checked_version, target_version)}
