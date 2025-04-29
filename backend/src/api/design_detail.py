from fastapi import APIRouter

from src.controllers import design_detail_controller
from src.models.design_detail import DesignDetailRequest, DesignDetailResponse

router = APIRouter()


@router.post("/design_detail", response_model=DesignDetailResponse)
def generate_design_detail(request: DesignDetailRequest):
    """
    設計概要リクエストを受け取り、設計詳細レスポンスを返すエンドポイント。

    Parameters
    ----------
    request : DesignDetailRequest
        設計概要を含むリクエストモデル。

    Returns
    -------
    DesignDetailResponse
        生成された設計詳細を含むレスポンスモデル。
    """
    return design_detail_controller.generate_design_detail(request)
