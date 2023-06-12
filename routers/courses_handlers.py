from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import courses, students, groups
from schemas import ResponseModel, Course, Student
from utils import create_new_element, get_element, get_elements_list

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


# 3.6
@router.post("/", response_model=ResponseModel)
async def create_new_course(data: Course, session: AsyncSession = Depends(get_async_session)):
    """создать новый курс"""
    await create_new_element(session, courses, data)
    return ResponseModel(entity='course', data=data)


# 3.7
@router.get("/{course_id}", response_model=ResponseModel)
async def get_course_by_id(course_id: int, session: AsyncSession = Depends(get_async_session)):
    """получить данные о курсе по id"""
    c = await get_element(session, courses, course_id)
    course = Course(
        course_name=c.course_name
    ) if c else None
    return ResponseModel(entity='course', data=course)


# 3.8
@router.get("/{course_id}/students", response_model=ResponseModel)
async def get_students_list_by_course_id(course_id: int, session: AsyncSession = Depends(get_async_session)):
    """получить список всех студентов на курсе"""
    students_list = await get_elements_list(session, students)
    groups_list = await get_elements_list(session, groups)
    groups_list = [g.id for g in groups_list if g.course_id == course_id]
    students_list = [Student(
        first_name=s.first_name,
        last_name=s.last_name,
        group_id=s.group_id
    ) for s in students_list if s.group_id in groups_list]
    students_list = students_list if students_list else None
    return ResponseModel(entity='student', data=students_list)

