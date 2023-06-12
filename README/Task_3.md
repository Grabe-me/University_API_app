## Часть 3.

### Задачи:
1. Реализовать точки входа API должна быть с использованием FastAPI, включая входные и выходные модели Pydantic для каждого маршрута:
2. Написать инструкции по установке и запуску приложения.
3. Написать инструкции по использованию API.
___________________________________________________
#
### 1. Точки входа API.
#### Эндпоинты точек входа расположены в соответствующих файлах:

    /routers/students_handlers.py
* `POST /students` - создать нового студента.
* `GET /students/{student_id}` - получить информацию о студенте по его id.
* `PUT /students/{student_id}` - обновить информацию о студенте по его id.
* `DELETE /students/{student_id}` - удалить студента по его id.


    /routers/teachers_handlers.py
  * `GET /teachers` - получить список всех преподавателей.


    /routers/courses_handlers.py
* `POST /courses` - создать новый курс.
* `GET /courses/{course_id}` - получить информацию о курсе по его id.
* `GET /courses/{course_id}/students` - получить список всех студентов на курсе.
   
 
    /routers/grades_handlers.py
* `POST /grades` - создать новую оценку для студента по курсу.
* `PUT /grades/{grade_id}` - обновить оценку студента по курсу.
#
### 2. Инструкции по установке и запуску приложения.

#### Системные требования:

* OS Linux или LinuxVM (виртуальная машина).
* Необходимо наличие СУБД PostgreSQL.
* Необходимо наличие интерпретатора Python (версия 3.9 и выше).
* Необходимо наличие установщика PyPI (pip). 

#### Установка:

* Скопируйте репозиторий локально.
* В PostgresSQL создайте Базу Данных.
* В Базе Данных создайте Таблицы.
 

    -- Создание таблиц.

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

* Наполните Таблицы необходимой информацией.
    

    -- Напонение таблиц.
    -- Дополните данные по желанию [НЕобязательно].

    INSERT INTO Departments (department_name)
    VALUES
    ('Очное отделение'),
    ('Заочное отделение');
    
    INSERT INTO Faculties (faculty_name)
    VALUES
    ('Технический факультет'),
    ('Гуманитарный факультет');
    
    INSERT INTO Buildings (building_number)
    VALUES
    (1),
    (2),
    (3);
    
    INSERT INTO Classrooms (room_number, building_id)
    VALUES
    ('Аудитория 101', 1),
    ('Аудитория 102', 1),
    ('Аудитория 201', 2),
    ('Аудитория 202', 2),
    ('Аудитория 301', 3),
    ('Аудитория 302', 3);
    
    INSERT INTO Courses (course_name)
    VALUES
    ('Математика'),
    ('История'),
    ('Информатика'),
    ('Физика');
    
    INSERT INTO CoursePrograms (program)
    VALUES
    ('Программа_1'),
    ('Программа_2');
    
    INSERT INTO Teachers (first_name, last_name)
    VALUES
    ('Никола', 'Тесла'),
    ('Альберт', 'Эйнштейн');
    
    INSERT INTO Semesters (start_date, end_date)
    VALUES
    ('2023-01-01', '2023-06-30'),
    ('2023-07-01', '2023-12-31');
    
    INSERT INTO Groups (group_name, course_id, faculty_id, department_id)
    VALUES
    ('Группа_1_Оч', 1, 1, 1),
    ('Группа_1_Зч', 1, 1, 2),
    ('Группа_2_Оч', 2, 2, 1),
    ('Группа_3_Оч', 3, 2, 1);
    
    INSERT INTO Students (first_name, last_name, group_id)
    VALUES
    ('Иван', 'Иванов', 1),
    ('Степан', 'Степанов', 1),
    ('Петр', 'Петров', 2),
    ('Филипп', 'Филиппов', 2),
    ('Андрей', 'Андреев', 3),
    ('Никита', 'Никитин', 3),
    ('Алексей', 'Алексеев', 4),
    ('Григорий', 'Гришин', 4);
    
    INSERT INTO Schedules (group_id, teacher_id, classroom_id, date, start_time, end_time, subject)
    VALUES
    (1, 1, 1, '2023-01-01', '09:00:00', '10:30:00', 'Теоретическая механника'),
    (2, 2, 2, '2023-01-02', '09:00:00', '11:30:00', 'Высшая математика'),
    (3, 1, 4, '2023-01-02', '12:00:00', '13:30:00', 'Теоретическая механника'),
    (4, 2, 6, '2023-01-02', '12:00:00', '13:30:00', 'Высшая математика');
    
    INSERT INTO Exams (exam_date, course_id, group_id, classroom_id, semester_id)
    VALUES
    ('2023-06-01', 1, 1, 1, 1),
    ('2023-06-02', 2, 2, 2, 2);
    
    INSERT INTO Grades (student_id, exam_id, grade)
    VALUES
    (1, 1, 5),
    (2, 2, 4);
    
    INSERT INTO Assignments (assignment_name, description, date_added, group_id)
    VALUES
    ('Задание_1', 'Описание задания № 1', '2023-01-01', 1),
    ('Задание_2', 'Описание задания № 2', '2023-01-02', 2),
    ('Задание_3', 'Описание задания № 3', '2023-01-03', 3),
    ('Задание_4', 'Описание задания № 4', '2023-01-04', 4),
    ('Задание_5', 'Описание задания № 5', '2021-01-05', 1),
    ('Задание_6', 'Описание задания № 6', '2021-01-06', 2);
    
    INSERT INTO Curriculum (course_id, semester_id, program_id)
    VALUES
    (1, 1, 1),
    (2, 2, 2);

* Измените конфигурацию подключения к Базе Данных в файле `.env` (в корневом каталоге репозитория).
* В корневом каталоге репозитория создайте виртуальную среду:

      -- Переход в коревую директорию скачанного репозитория
        
      cd path/to/repository/root/dir


      -- Создание виртуальной среды

      python -m venv c:\path\to\myenv
* Запустите установку необходимых библиотек:

      -- Установка библиотек

      pip install --no-cache-dir -r requirements.txt

#### Запуск:

В корневом каталоге репозитория введите команду для запуска:

      gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --reload
#
### 3. Инструкции по использованию API.

* Доступ к API приложению на локальной машине реализован по адресу:
    
    
    -- Подставьте соответствующие точки входа, указанные в 1 пункте

    0.0.0.0:8000/<точка входа>

* Взаимодействие с приложением посредством веб-интерфейса возможно по адресу:


    -- Отображение документации в формате Swagger

    0.0.0.0:8000/docs

    -- Отображение документации в формате ReDoc

    0.0.0.0:8000/redoc
