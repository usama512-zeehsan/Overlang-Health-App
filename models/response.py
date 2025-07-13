from pydantic import BaseModel
from typing import List, Optional

class Recommendation(BaseModel):
    goal: str
    tips: List[str]
    products: List[str]
    call_to_action: Optional[str] = None
