from fastapi.encoders import jsonable_encoder
from routers.students_handlers import router as students_router
from routers.teachers_handlers import router as teachers_router
from routers.courses_handlers import router as courses_router
from routers.grades_handlers import router as grades_router
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


"""
1. students Студент
2. teachers Преподаватель
3. courses Курс
4. groups Группа
5. departments Отделение (очное - заочное)
6. grades Оценка
7. schedules Расписание
8. buildings Здание
9. classrooms Аудитория
10. semesters Семестр
11. faculties Факультет
12. exams Экзамен
13. assignments Задание для самостоятельной работ
14. courses Program Программа курса
15. curriculum Учебный план
"""


app = FastAPI(title="University")

app.include_router(students_router)
app.include_router(teachers_router)
app.include_router(courses_router)
app.include_router(grades_router)


@app.exception_handler(Exception)
async def my_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({'detail': exc.args})
    )
