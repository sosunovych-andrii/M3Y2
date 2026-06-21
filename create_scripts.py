import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
    """
)


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(100),
        instructor VARCHAR(300)
    )
    """
)


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS student_courses(
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    )
    """
)


conn.commit()