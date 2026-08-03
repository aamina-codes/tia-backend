from pydantic import BaseModel
from typing import Optional


class ThyroidTest(BaseModel):

    value: Optional[float] = None

    unit: Optional[str] = None

    reference_range: Optional[str] = None

    status: Optional[str] = None


class ThyroidProfile(BaseModel):

    TSH: Optional[ThyroidTest] = None

    FT3: Optional[ThyroidTest] = None

    FT4: Optional[ThyroidTest] = None

    T3: Optional[ThyroidTest] = None

    T4: Optional[ThyroidTest] = None

    Anti_TPO: Optional[ThyroidTest] = None