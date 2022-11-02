from fastapi import APIRouter

from shatoru_backend import schemas

router = APIRouter()


@router.get("/health", response_model=schemas.Health)
async def health():
    return {"status": "OK"}
