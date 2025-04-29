from fastapi import APIRouter

from src.controllers import mermaid_controller
from src.models.mermaid import MermaidRequest, MermaidResponse

router = APIRouter()


@router.post("/mermaid", response_model=MermaidResponse)
def generate_mermaid(request: MermaidRequest):
    """
    Mermaid記法生成リクエストを受け取り、Mermaid記法レスポンスを返すエンドポイント。

    Parameters
    ----------
    request : MermaidRequest
        Mermaid記法生成のためのリクエストモデル。

    Returns
    -------
    MermaidResponse
        生成されたMermaid記法の図を含むレスポンスモデル。
    """
    return mermaid_controller.generate_mermaid(request)
