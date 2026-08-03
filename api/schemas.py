from pydantic import BaseModel
from typing import Any, Dict, List


class AnalysisResponse(BaseModel):

    thyroid_values: Dict[str, Any]

    analysis: Dict[str, Any]

    risk: Dict[str, Any]

    possible_conditions: List[Dict[str, Any]]

    recommendations: List[str]

    summary: str