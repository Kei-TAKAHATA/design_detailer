from pydantic import BaseModel


class MermaidRequest(BaseModel):
    design_detail: str
    count: int | None = None


class MermaidResponse(BaseModel):
    mermaid: str
