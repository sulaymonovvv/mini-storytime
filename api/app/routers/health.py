from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    # Faqat «ilova tirikmi?» ni tekshiradi, bazaga bormaydi.
    return {"status": "ok"}
