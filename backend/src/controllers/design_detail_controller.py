from src.services import design_detail_service
from src.models.design_detail import DesignDetailRequest, DesignDetailResponse


def generate_design_detail(request: DesignDetailRequest) -> DesignDetailResponse:
    design_summary = request.design_summary
    design_detail = design_detail_service.generate_design_detail(design_summary)
    return DesignDetailResponse(design_detail=design_detail)
