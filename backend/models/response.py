from typing import List, Optional
from pydantic import BaseModel


class ReportImage(BaseModel):
    image_url: str
    source: str
    source_url: str


class ReportSection(BaseModel):
    title: str
    content: str
    image: Optional[ReportImage] = None


class ResearchResponse(BaseModel):
    report: str

    hero: Optional[ReportImage] = None

    sections: List[ReportSection]

    report_path: str

    ppt_path: str