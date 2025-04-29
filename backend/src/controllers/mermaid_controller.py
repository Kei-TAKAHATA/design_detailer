from src.services import mermaid_service
from src.models.mermaid import MermaidRequest, MermaidResponse


def generate_mermaid(request: MermaidRequest) -> MermaidResponse:
    mermaid = mermaid_service.convert_design_detail_to_mermaid(
        request.design_detail,
        request.count
    )
    return MermaidResponse(mermaid=mermaid)
