SELECT students.fullname, grades.grade
FROM grades 
JOIN students ON grades.student_id = students.id
WHERE students.group_id = 2
AND grades.subject_id = 2
AND grades.grade_date = (
SELECT MAX(grades.grade_date)
FROM grades 
WHERE grades.subject_id = 6
);