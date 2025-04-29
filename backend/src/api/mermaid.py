from fastapi import APIRouter

from src.controllers import mermaid_controller
from src.models.mermaid import MermaidRequest, MermaidResponse

router = APIRouter()


@router.post("/mermaid", response_model=MermaidResponse)
def generate_mermaid(request: MermaidRequest):
    return mermaid_controller.generate_mermaid(request)
