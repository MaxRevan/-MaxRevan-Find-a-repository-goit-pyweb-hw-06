SELECT s.fullname, AVG(g.grade) AS average_grade
FROM students s 
JOIN grades g on s.id = g.student_id 
WHERE g.subject_id = 3
GROUP BY s.id
ORDER BY AVG(g.grade) DESC
LIMIT 1;