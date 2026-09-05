import sqlite3
from datetime import datetime


def mark_attendance(college_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Student ko college id se search karo
    cursor.execute(
        "SELECT name FROM students WHERE college_id = ?", (college_id,)
    )
    student = cursor.fetchone()

    if student:
        name = student[0]

        # Current date aur time
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        # Attendance table banana (Ekdum sahi syntax)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                college_id TEXT NOT NULL,
                attendance_date TEXT NOT NULL,
                attendance_time TEXT NOT NULL
            )
        """)

        # Attendance insert karna (Ekdum single line bina kisi error ke)
        cursor.execute(
            "INSERT INTO attendance (name, college_id, attendance_date, attendance_time) VALUES (?, ?, ?, ?)",
            (name, college_id, current_date, current_time),
        )

        connection.commit()
        print("\nAttendance marked successfully! ✅")
        print("Name:", name)
        print("College ID:", college_id)
        print("Date:", current_date)
        print("Time:", current_time)
    else:
        print("\nStudent not found! ❌")

    connection.close()


# User se input lena
college_id = input("enter COLLEGE ID: ")
mark_attendance(college_id)