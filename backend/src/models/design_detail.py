from pydantic import BaseModel


class DesignDetailRequest(BaseModel):
    design_summary: str


class DesignDetailResponse(BaseModel):
    design_detail: str
