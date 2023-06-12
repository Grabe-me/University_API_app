from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import grades
from schemas import ResponseModel, Grade
from utils import create_new_element, update_element

router = APIRouter(
    prefix="/grades",
    tags=["Grades"]
)


# 3.9
@router.post("/grades", response_model=ResponseModel)
async def create_new_grade(data: Grade, session: AsyncSession = Depends(get_async_session)):
    """создать новую оценку ученику"""
    await create_new_element(session, grades, data)
    return ResponseModel(entity='grade', data=data)


# 3.10
@router.put("/grades/{grade_id}", response_model=ResponseModel)
async def update_grade_by_id(grade_id, data: Grade, session: AsyncSession = Depends(get_async_session)):
    """обновить оценку по id"""
    await update_element(session, grades, data, grade_id)
    return ResponseModel(entity='grade', data=data)
