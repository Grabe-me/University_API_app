## Часть 1:

### Задачи:
1) Необходимо создать схему базы данных, состоящую из 15 сущностей:
   * Студент
   * Преподаватель
   * Курс
   * Группа
   * Отделение
   * Оценка
   * Расписание
   * Здание
   * Аудитория
   * Семестр
   * Факультет
   * Экзамен
   * Задание для самостоятельной работы
   * Программа курса
   * Учебный план
 

2) Создать ER-диаграмму (схему связей между сущностями) и определить свойства каждой из этих сущностей.


3) Написать SQL запросы для создания соответствующих таблиц, включающих все необходимые поля и связи между ними.
__________________________________________
#
### 1. ER-диаграмма.
#### Диаграмма расположена в директории `README/diagram`

Формат PNG:
* "ERD_University.png"

Формат ERD:
* "ERD_University.erd"
#
### 2. Описание таблиц

1. Таблица "Студенты":
   - Идентификатор студента (PK)
   - Имя
   - Фамилия
   - Группа (FK: Идентификатор группы)

2. Таблица "Преподаватели":
   - Идентификатор преподавателя (PK)
   - Имя
   - Фамилия

3. Таблица "Курсы":
   - Идентификатор курса (PK)
   - Название курса

4. Таблица "Группы":
   - Идентификатор группы (PK)
   - Номер группы
   - Курс (FK: Идентификатор курса)
   - Факультет (FK: Идентификатор факультета)
   - Отделение (FK: Идентификатор отделения)

5. Таблица "Отделения":
   - Идентификатор курса (PK)
   - Название отделения

6. Таблица "Оценки":
   - Идентификатор оценки (PK)
   - Студент (FK: Идентификатор студента)
   - Экзамен (FK: Идентификатор экзамена)
   - Оценка

7. Таблица "Расписание":
   - Идентификатор расписания (PK)
   - Группа (FK: Идентификатор группы)
   - Преподаватель (FK: Идентификатор преподавателя)
   - Аудитория (FK: Идентификатор аудитории)
   - Дата
   - Время начала
   - Время окончания
   - Предмет

8. Таблица "Здания":
   - Идентификатор здания (PK)
   - Номер здания

9. Таблица "Аудитории":
   - Идентификатор аудитории (PK)
   - Номер аудитории
   - Здание (FK: Идентификатор здания)

10. Таблица "Семестры":
    - Идентификатор семестра (PK)
    - Дата начала
    - Дата окончания

11. Таблица "Факультеты":
    - Идентификатор факультета (PK)
    - Название факультета

12. Таблица "Экзамены":
    - Идентификатор экзамена (PK)
    - Дата
    - Предмет
    - Группа (FK: Идентификатор группы)
    - Аудитория (FK: Идентификатор аудитории)
    - Семестр (FK: Идентификатор семестра)

13. Таблица "Задания для самостоятельной работы":
    - Идентификатор задания (PK)
    - Название задания
    - Описание
    - Дата добавления
    - Группа (FK: Идентификатор группы)

14. Таблица "Программы курсов":
    - Идентификатор программы курса (PK)
    - Программа

15. Таблица "Учебные планы":
    - Идентификатор учебного плана (PK)
    - Курс (FK: Идентификатор курса)
    - Семестр (FK: Идентификатор семестра)
    - Программа курса (FK: Идентификатор программы курса)
#
### 3. SQL запросы для создания таблиц (PostgreSQL).

    CREATE TABLE Departments (
        id SERIAL PRIMARY KEY,
        department_name VARCHAR(255) NOT NULL UNIQUE
    );
    
    CREATE TABLE Faculties (
        id SERIAL PRIMARY KEY,
        faculty_name VARCHAR(255) NOT NULL UNIQUE
    );
    
    CREATE TABLE Buildings (
        id SERIAL PRIMARY KEY,
        building_number INTEGER NOT NULL UNIQUE CHECK (building_number > 0)
    );
    
    CREATE TABLE Classrooms (
        id SERIAL PRIMARY KEY,
        room_number VARCHAR(50) NOT NULL,
        building_id INTEGER REFERENCES Buildings(id) NOT NULL CHECK (building_id > 0)
    );
    
    CREATE TABLE Courses (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(255) NOT NULL UNIQUE
    );
    
    CREATE TABLE CoursePrograms (
        id SERIAL PRIMARY KEY,
        program TEXT NOT NULL UNIQUE
    );
    
    CREATE TABLE Teachers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL
    );
    
    CREATE TABLE Semesters (
        id SERIAL PRIMARY KEY,
        start_date DATE NOT NULL UNIQUE,
        end_date DATE NOT NULL UNIQUE
    );
    
    CREATE TABLE Groups (
        id SERIAL PRIMARY KEY,
        group_name VARCHAR(50) NOT NULL UNIQUE,
        course_id INTEGER REFERENCES Courses(id) NOT NULL CHECK (course_id > 0),
        faculty_id INTEGER REFERENCES Faculties(id) NOT NULL CHECK (faculty_id > 0),
        department_id INTEGER REFERENCES Departments(id) NOT NULL CHECK (department_id > 0)
    );
    
    CREATE TABLE Students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        group_id INTEGER REFERENCES Groups(id) NOT NULL CHECK (group_id > 0)
    );
    
    CREATE TABLE Schedules (
        id SERIAL PRIMARY KEY,
        group_id INTEGER REFERENCES Groups(id) NOT NULL CHECK (group_id > 0),
        teacher_id INTEGER REFERENCES Teachers(id) NOT NULL CHECK (teacher_id > 0),
        classroom_id INTEGER REFERENCES Classrooms(id) NOT NULL CHECK (classroom_id > 0),
        date DATE NOT NULL,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        subject VARCHAR(255) NOT NULL
    );
    
    CREATE TABLE Exams (
        id SERIAL PRIMARY KEY,
        exam_date DATE NOT NULL,
        course_id INTEGER REFERENCES Courses(id) NOT NULL CHECK (course_id > 0),
        group_id INTEGER REFERENCES Groups(id) NOT NULL CHECK (group_id > 0),
        classroom_id INTEGER REFERENCES Classrooms(id) NOT NULL CHECK (classroom_id > 0),
        semester_id INTEGER REFERENCES Semesters(id) NOT NULL CHECK (semester_id > 0)
    );
    
    CREATE TABLE Grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES Students(id) NOT NULL CHECK (student_id > 0),
        exam_id INTEGER REFERENCES Exams(id) NOT NULL CHECK (exam_id > 0),
        grade INTEGER NOT NULL CHECK (grade > 0 AND grade <= 5)
    );
    
    CREATE TABLE Assignments (
        id SERIAL PRIMARY KEY,
        assignment_name VARCHAR(255) NOT NULL UNIQUE,
        description TEXT,
        date_added DATE DEFAULT CURRENT_DATE,
        group_id INTEGER REFERENCES Groups(id) NOT NULL CHECK (group_id > 0)
    );
    
    CREATE TABLE Curriculum (
        id SERIAL PRIMARY KEY,
        course_id INTEGER REFERENCES Courses(id) NOT NULL CHECK (course_id > 0),
        semester_id INTEGER REFERENCES Semesters(id) NOT NULL CHECK (semester_id > 0),
        program_id INTEGER REFERENCES CoursePrograms(id) NOT NULL CHECK (program_id > 0)
    );
