from pydantic import BaseModel
from typing import Optional


class Patient(BaseModel):

    name: Optional[str] = None

    age: Optional[int | str] = None

    gender: Optional[str] = None