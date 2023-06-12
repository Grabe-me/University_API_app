from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text, Table, MetaData


metadata = MetaData()


departments = Table(
    "departments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("department_name", String(255), unique=True)
)

faculties = Table(
    "faculties",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("faculty_name", String(255), unique=True)
)

buildings = Table(
    "buildings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("building_number", Integer, unique=True)
)

classrooms = Table(
    "classrooms",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("room_number", String(50)),
    Column("building_id", Integer, ForeignKey("buildings.id"))
)

courses = Table(
    "courses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("course_name", String(255), unique=True)
)

course_programs = Table(
    "course_programs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("program", Text, unique=True)
)

teachers = Table(
    "teachers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(255)),
    Column("last_name", String(255))
)

semesters = Table(
    "semesters",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("start_date", Date, unique=True),
    Column("end_date", Date, unique=True)
)

groups = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_name", String(50), unique=True),
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("faculty_id", String(255), ForeignKey("faculties.id")),
    Column("department_id", String(255), ForeignKey("departments.id"))
)

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("group_id", Integer, ForeignKey("groups.id"))
)

schedules = Table(
    "schedules",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("classroom_id", Integer, ForeignKey("classrooms.id")),
    Column("date", Date),
    Column("start_time", Time),
    Column("end_time", Time),
    Column("subject", String(255))
)

exams = Table(
    "exams",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("exam_date", Date),
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("classroom_id", Integer, ForeignKey("classrooms.id")),
    Column("semester_id", Integer, ForeignKey("semesters.id"))
)

grades = Table(
    "grades",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("exam_id", Integer, ForeignKey("exams.id")),
    Column("grade", Integer)
)

assignments = Table(
    "assignments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("assignment_name", String(255), unique=True),
    Column("description", Text),
    Column("date_added", Date, default=datetime.now()),
    Column("group_id", Integer, ForeignKey("groups.id"))
)

curriculum = Table(
    "curriculum",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("semester_id", Integer, ForeignKey("semesters.id")),
    Column("program_id", Integer, ForeignKey("course_programs.id"))
)
