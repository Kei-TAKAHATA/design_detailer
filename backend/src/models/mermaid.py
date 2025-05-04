from pydantic import BaseModel


class MermaidRequest(BaseModel):
    """
    Mermaid記法の生成リクエストモデル。

    Attributes
    ----------
    design_detail : str
        設計詳細のテキスト。
    """
    design_detail: str


class MermaidResponse(BaseModel):
    """
    Mermaid記法の生成レスポンスモデル。

    Attributes
    ----------
    mermaid : str
        生成されたMermaid記法の図。
    """
    mermaid: str
