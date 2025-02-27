from pydantic import BaseModel
from typing import Optional, Any

class APIResponse(BaseModel):
    status_code: int
    data: Optional[Any] = None
    error: Optional[str] = None
    message: Optional[str] = None
