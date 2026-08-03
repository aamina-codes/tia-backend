from pydantic import BaseModel

from schemas.patient import Patient
from schemas.report import ReportInfo
from schemas.thyroid_profile import ThyroidProfile
from schemas.analysis import Analysis
from schemas.history import History


class ReportResponse(BaseModel):

    patient: Patient

    report: ReportInfo

    thyroid_profile: ThyroidProfile

    analysis: Analysis

    risk: dict

    possible_conditions: list

    recommendations: list[str]

    red_flags: list

    summary: str


class APIResponse(BaseModel):

    success: bool

    message: str

    report: ReportResponse

    history: History