from fastapi import APIRouter
from models import EvElani

router = APIRouter()

# Fake database (hələlik)
database = []

@router.get("/elanlar")
def elanlari_getir():
    return database

@router.post("/elan_yarat")
def elan_yarat(elan: EvElani):
    elan.id = len(database) + 1
    database.append(elan)
    return {"status": "ok", "message": "Elan əlavə olundu", "data": elan}
