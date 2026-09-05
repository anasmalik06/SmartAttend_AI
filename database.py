import sqlite3


def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            college_id TEXT UNIQUE NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database and students table created successfully!")


create_database()