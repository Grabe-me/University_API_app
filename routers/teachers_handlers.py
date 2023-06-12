from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import teachers
from schemas import ResponseModel, Teacher
from utils import get_elements_list

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


# 3.5
@router.get("/", response_model=ResponseModel)
async def get_teachers_list(session: AsyncSession = Depends(get_async_session)):
    """получить список всех учителей"""
    teachers_list = await get_elements_list(session, teachers)
    teachers_list = [
        Teacher(
            first_name=t.first_name,
            last_name=t.last_name
        ) for t in teachers_list if t
    ]
    return ResponseModel(entity='teacher', data=teachers_list)
