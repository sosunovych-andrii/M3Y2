import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def add_student():
    name = input("Name:")
    age = input("Age:")
    major = input("Major:")

    cursor.execute(
        "INSERT INTO students(name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    conn.commit()


def add_course():
    course_name = input("Course:")
    instructor = input("Instructor:")

    cursor.execute(
        "INSERT INTO courses(course_name, instructor) VALUES (?, ?)",
        (course_name, instructor)
    )
    conn.commit()


def show_students():
    cursor.execute("SELECT * FROM students")

    for student in cursor.fetchall():
        print(student)


def show_courses():
    cursor.execute("SELECT * FROM courses")

    for course in cursor.fetchall():
        print(course)


def register_student():
    student_id = int(input("ID student:"))
    course_id = int(input("ID course:"))

    cursor.execute(
        "INSERT INTO student_courses(student_id, course_id) VALUES(?, ?)",
        (student_id, course_id)
    )
    conn.commit()


def main():
    while True:
        choice = input("Choice:")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            register_student()
        elif choice == "4":
            show_students()
        elif choice == "5":
            show_courses()
        else:
            break
    conn.close()


if __name__ == "__main__":
    main()
