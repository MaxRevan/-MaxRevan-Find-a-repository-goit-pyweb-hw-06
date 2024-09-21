queries = {
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    1: """SELECT s.fullname, AVG(g.grade) AS average_grade
          FROM students s 
          JOIN grades g on s.id = g.student_id 
          GROUP by s.id 
          ORDER by average_grade desc 
          LIMIT 5;""",

    # Знайти студента із найвищим середнім балом з певного предмета
    2: """SELECT s.fullname, AVG(g.grade) AS average_grade
          FROM students s 
          JOIN grades g on s.id = g.student_id 
          WHERE g.subject_id = %s
          GROUP BY s.id
          ORDER BY average_grade DESC
          LIMIT 1;""",

    # Знайти середній бал у групах з певного предмета
    3: """SELECT g.name AS group_name, AVG(gr.grade) AS average_grade
          FROM "groups" g 
          JOIN students s ON g.id = s.group_id 
          JOIN grades gr ON s.id = gr.student_id 
          WHERE gr.subject_id = %s
          GROUP BY g.id;""",

    # Знайти середній бал на потоці (по всій таблиці оцінок)
    4: """SELECT AVG(g.grade) AS average_grade
          FROM grades g;""",
 
    # Знайти які курси читає певний викладач
    5: """SELECT s.name
          FROM subjects s 
          WHERE teacher_id = %s;""",

    # Знайти список студентів у певній групі.
    6: """SELECT s.fullname AS studets_name
          FROM students s 
          WHERE group_id = %s;""",

    # Знайти оцінки студентів у окремій групі з певного предмета
    7: """SELECT s.fullname, g.grade
          FROM students s
          JOIN grades g ON s.id = g.student_id
          WHERE s.group_id = %s AND g.subject_id = %s;""",

    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    8: """SELECT AVG(g.grade) AS average_grade
          FROM grades g 
          JOIN subjects sub ON g.subject_id = sub.id
          WHERE sub.teacher_id = %s;""",

    # Знайти список курсів, які відвідує студент
    9: """SELECT sub.name
          FROM subjects sub
          JOIN grades g ON sub.id = g.subject_id
          WHERE g.student_id = %s;""",   
   
    # Список курсів, які певному студенту читає певний викладач
    10: """SELECT sub.name
           FROM subjects sub
           JOIN grades g ON sub.id = g.subject_id
           WHERE g.student_id = %s and sub.teacher_id = %s;""",

    # Середній бал, який певний викладач ставить певному студентові
    11: """SELECT AVG(gr.grade) AS average_grade
           FROM grades gr 
           JOIN subjects sub ON gr.subject_id = sub.id
           JOIN teachers t ON sub.teacher_id = t.id
           WHERE gr.student_id = %s and t.id = %s;""",          

    # Оцінки студентів у певній групі з певного предмета на останньому занятті
    12: """SELECT students.fullname, grades.grade
           FROM grades 
           JOIN students ON grades.student_id = students.id
           WHERE students.group_id = %s
           AND grades.subject_id = %s
           AND grades.grade_date = (
           SELECT MAX(grades.grade_date)
           FROM grades 
           WHERE grades.subject_id = %s
           );"""
}

    

