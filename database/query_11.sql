SELECT AVG(gr.grade) AS average_grade
FROM grades gr 
JOIN subjects sub ON gr.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE gr.student_id = 23 and t.id = 5;