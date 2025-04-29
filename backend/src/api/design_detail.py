from fastapi import APIRouter

from src.controllers import design_detail_controller
from src.models.design_detail import DesignDetailRequest, DesignDetailResponse

router = APIRouter()


@router.post("/design_detail", response_model=DesignDetailResponse)
def generate_design_detail(request: DesignDetailRequest):
    return design_detail_controller.generate_design_detail(request)
