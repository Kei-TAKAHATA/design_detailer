from src.services import mermaid_service
from src.models.mermaid import MermaidRequest, MermaidResponse


def generate_mermaid(request: MermaidRequest) -> MermaidResponse:
    """
    Mermaid記法生成リクエストからMermaid記法レスポンスを生成する。

    Parameters
    ----------
    request : MermaidRequest
        Mermaid記法生成のためのリクエストモデル。

    Returns
    -------
    MermaidResponse
        生成されたMermaid記法の図を含むレスポンスモデル。
    """
    mermaid = mermaid_service.convert_design_detail_to_mermaid(
        design_detail=request.design_detail,
    )
    return MermaidResponse(mermaid=mermaid)
