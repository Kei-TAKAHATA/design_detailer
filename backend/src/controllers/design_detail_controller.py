from src.services import design_detail_service
from src.models.design_detail import DesignDetailRequest, DesignDetailResponse


def generate_design_detail(request: DesignDetailRequest) -> DesignDetailResponse:
    """
    設計概要リクエストから設計詳細レスポンスを生成する。

    Parameters
    ----------
    request : DesignDetailRequest
        設計概要を含むリクエストモデル。

    Returns
    -------
    DesignDetailResponse
        生成された設計詳細を含むレスポンスモデル。
    """
    design_summary = request.design_summary
    design_detail = design_detail_service.generate_design_detail(design_summary)
    return DesignDetailResponse(design_detail=design_detail)
