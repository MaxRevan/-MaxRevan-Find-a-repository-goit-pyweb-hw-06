import logging
import psycopg2
from faker import Faker
import random
from psycopg2 import DatabaseError

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(host="localhost", database="univer", user="postgres", password="12345")
cur = conn.cursor()

# Додавання груп
group_names = ['Group 113', 'Group 123', 'Group 133']
for group_name in group_names:
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (group_name,))

# Додавання викладачів
for _ in range(5):
    cur.execute("INSERT INTO teachers (fullname) VALUES (%s)", (fake.name(),))

# Додавання предметів із вказівкою викладача
subject_names = ['Mathematics', 'Physics', 'Chemistry', 'History', 'Biology', 'Geography']
teacher_ids = list(range(1, 6))
for subject_name in subject_names:
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", 
                (subject_name, random.choice(teacher_ids)))

# Додавання студентів і оцінок
student_count = 50
subject_count = len(subject_names)
for group_id in range(1, 4):
    for _ in range(student_count // 3):
        cur.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id", 
                    (fake.name(), group_id))
        student_id = cur.fetchone()[0]
        for subject_id in range(1, subject_count + 1): 
            for _ in range(random.randint(15, 20)):
                cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                                        (student_id, subject_id, random.randint(0, 100), fake.date_this_year()))


try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()