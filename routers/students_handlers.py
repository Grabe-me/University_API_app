from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import students
from schemas import ResponseModel, Student
from utils import create_new_element, get_element, update_element, delete_element

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 3.1
@router.post("/", response_model=ResponseModel)
async def create_new_student(data: Student, session: AsyncSession = Depends(get_async_session)):
    """создать нового студента с занесением в БД"""
    await create_new_element(session, students, data)
    return ResponseModel(entity='student', data=data)


# 3.2
@router.get("/{student_id}", response_model=ResponseModel)
async def get_student_by_id(student_id: int, session: AsyncSession = Depends(get_async_session)):
    """получить информацию о студенте по id"""
    s = await get_element(session, students, student_id)
    student = Student(
        first_name=s.first_name,
        last_name=s.last_name,
        group_id=s.group_id
    ) if s else None
    student = student if student else []
    return ResponseModel(entity='student', data=student)


# 3.3
@router.put("/{student_id}", response_model=ResponseModel)
async def update_student_by_id(student_id: int, data: Student, session: AsyncSession = Depends(get_async_session)):
    """обновить информацию о студенте по id"""
    await update_element(session, students, data, student_id)
    return ResponseModel(entity='student', data=data)


# 3.4
@router.delete("/{student_id}", response_model=ResponseModel)
async def delete_student_by_id(student_id: int, session: AsyncSession = Depends(get_async_session)):
    """удалить информацию о студенте по id"""
    await delete_element(session, students, student_id)
    return ResponseModel(entity='student')
