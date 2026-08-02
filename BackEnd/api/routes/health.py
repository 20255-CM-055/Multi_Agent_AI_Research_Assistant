from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Welcome to the Multi-Agent AI Research Assistant API 🚀"
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }