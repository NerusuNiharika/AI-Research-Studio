from pydantic import BaseModel


class ResearchResponse(BaseModel):
    report: str
    report_path: str
    ppt_path: str