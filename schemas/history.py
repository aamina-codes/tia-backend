from pydantic import BaseModel
from typing import Any


class History(BaseModel):

    total_reports: int

    timeline: list[Any]

    trends: dict

    insights: list[str]