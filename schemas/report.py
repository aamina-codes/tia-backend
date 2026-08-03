from pydantic import BaseModel
from typing import Optional


class ReportInfo(BaseModel):

    lab_name: Optional[str] = None

    report_date: Optional[str] = None

    doctor: Optional[str] = None