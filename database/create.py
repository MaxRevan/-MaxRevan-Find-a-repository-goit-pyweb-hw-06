import logging
from psycopg2 import DatabaseError
from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_create_groups_table = """
    drop table if exists groups;
    CREATE TABLE groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );
    """
    sql_create_students_table = """
    drop table if exists students;
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(150) NOT NULL,
        group_id INTEGER REFERENCES groups(id)
  	    on delete cascade
    );
    """
    sql_create_teachers_table = """
    drop table if exists teachers;
    CREATE TABLE teachers (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(150) NOT NULL
    );
    """
    sql_create_subjects_table = """
    drop table if exists subjects;
    CREATE TABLE subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        teacher_id INTEGER  REFERENCES teachers(id)
  	    on delete cascade
    );
    """

    sql_create_grades_table = """
    drop table if exists grades;
    CREATE TABLE grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER  REFERENCES students(id)
        on delete cascade,
        subject_id INTEGER  REFERENCES subjects(id)
        on delete cascade,
        grade INTEGER CHECK (grade >= 0 AND grade <= 100),
        grade_date DATE NOT NULL
    );
    """

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_groups_table)
                create_table(conn, sql_create_students_table)
                create_table(conn, sql_create_teachers_table)
                create_table(conn, sql_create_subjects_table)
                create_table(conn, sql_create_grades_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)