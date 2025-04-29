from pydantic import BaseModel


class DesignDetailRequest(BaseModel):
    """
    設計詳細リクエストモデル。

    Attributes
    ----------
    design_summary : str
        設計の概要テキスト。
    """
    design_summary: str


class DesignDetailResponse(BaseModel):
    """
    設計詳細レスポンスモデル。

    Attributes
    ----------
    design_detail : str
        生成された設計詳細テキスト。
    """
    design_detail: str
