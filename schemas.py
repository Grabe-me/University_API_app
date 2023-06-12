from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class Course(BaseModel):
    course_name: str = Field(max_length=150)

    class Config:
        orm_mode = True


class Student(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    group_id: int = Field(gt=0)

    class Config:
        orm_mode = True


class Teacher(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)

    class Config:
        orm_mode = True


class Grade(BaseModel):
    student_id: int = Field(ge=1)
    exam_id: int = Field(ge=1)
    grade: int = Field(ge=1, le=5)

    class Config:
        orm_mode = True


class Entity(Enum):
    student = 'student'
    teacher = 'teacher'
    course = 'course'
    grade = 'grade'


class ResponseModel(BaseModel):
    entity: Entity
    data: Any
