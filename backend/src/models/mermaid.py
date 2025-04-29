from pydantic import BaseModel


class MermaidRequest(BaseModel):
    """
    Mermaid記法の生成リクエストモデル。

    Attributes
    ----------
    design_detail : str
        設計詳細のテキスト。
    count : int, optional
        追加のオプション。2の場合は別パターンを返す。
    """
    design_detail: str
    count: int | None = None


class MermaidResponse(BaseModel):
    """
    Mermaid記法の生成レスポンスモデル。

    Attributes
    ----------
    mermaid : str
        生成されたMermaid記法の図。
    """
    mermaid: str
