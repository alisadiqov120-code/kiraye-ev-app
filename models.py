from pydantic import BaseModel
from typing import Optional

class EvElani(BaseModel):
    id: Optional[int]
    seher: str
    rayon: str
    otaq_sayi: int
    qiymet: float
    elan_veren: str
    telefon: str
