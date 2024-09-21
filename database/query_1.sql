SELECT s.fullname, AVG(g.grade) AS average_grad
FROM students s 
JOIN grades g on s.id = g.student_id 
GROUP by s.id 
ORDER by AVG(g.grade) desc 
LIMIT 5;