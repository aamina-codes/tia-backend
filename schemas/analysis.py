from pydantic import BaseModel
from typing import List


class Analysis(BaseModel):

    overall_status: str

    abnormal_tests: List[str]

    interpretation: str