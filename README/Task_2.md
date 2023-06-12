## Часть 2.

### Задача:
Составить соответствующие SQL запросы:
1) Выбрать всех студентов, обучающихся на курсе "Математика".

2) Обновить оценку студента по курсу.

3) Выбрать всех преподавателей, которые преподают в здании №3.

4) Удалить задание для самостоятельной работы, которое было создано более года назад.

5) Добавить новый семестр в учебный год.
____________________________________________
### SQL запросы (PostgreSQL):
1) Выбрать всех студентов обучающихся на курсе "Математика"

        SELECT s.id, s.first_name, s.last_name, c.course_name
        FROM Students s
        JOIN Groups g ON s.group_id = g.id
        JOIN Courses c ON g.course_id = c.id
        WHERE c.course_name = 'Математика';


2) Обновить оценку студента по курсу.

        UPDATE Grades
        SET grade = <новая_оценка>
        FROM Students s
        JOIN Groups g ON s.group_id = g.id
        JOIN Courses c ON g.course_id = c.id
        JOIN Exams e ON c.id = e.course_id
        WHERE s.id = <id_студента>
            AND c.course_id = <идентификатор_курса>;



3) Выбрать всех преподавателей, которые преподают в здании №3.

        SELECT t.first_name, t.last_name
        FROM Teachers t
        JOIN Schedules s ON t.id = s.teacher_id
        JOIN Classrooms c ON s.classroom_id = c.id
        JOIN Buildings b ON c.building_id = b.id
        WHERE b.building_number = 3;



4) Удалить задание для самостоятельной работы, которое было создано более года назад.

        DELETE FROM assignments
        WHERE date_added < CURRENT_DATE - INTERVAL '1 year';




5) Добавить новый семестр в учебный год.

        INSERT INTO Semesters (start_date, end_date)
        VALUES (<дата начала>, <дата окончания>);
