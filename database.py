import sqlite3

DB_NAME = 'database/gradebook.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    with connect_db() as conn:
        cursor = conn.cursor()

        # Students Table (starts at ID 100)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')

        # Courses Table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')

        # Grades Table (normalized to link student and course)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            subcategory TEXT,
            category TEXT,
            weight REAL,
            score REAL,
            weighted_score REAL,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
        ''')

        # Set starting student ID to 100 if table is empty
        cursor.execute('SELECT COUNT(*) FROM students')
        if cursor.fetchone()[0] == 0:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='students'")
            cursor.execute("INSERT INTO students (id, name) VALUES (?, ?)", (99, '__init__'))
            cursor.execute("DELETE FROM students WHERE id = 99")

        conn.commit()

def save_grade(student_name, course_name, df):
    with connect_db() as conn:
        cursor = conn.cursor()

        # Insert or get course
        cursor.execute("SELECT id FROM courses WHERE name = ?", (course_name,))
        course = cursor.fetchone()
        if course:
            course_id = course[0]
        else:
            cursor.execute("INSERT INTO courses (name) VALUES (?)", (course_name,))
            course_id = cursor.lastrowid

        # Insert student
        cursor.execute("INSERT INTO students (name) VALUES (?)", (student_name,))
        student_id = cursor.lastrowid

        # Insert grade data from dataframe
        for _, row in df.iterrows():
            cursor.execute('''
            INSERT INTO grades (student_id, course_id, subcategory, category, weight, score, weighted_score)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                student_id,
                course_id,
                row['Subcategory'],
                row['Category'],
                row['Weight (%)'],
                row['Subcategory Score (%)'],
                row['Weighted Score']
            ))

        conn.commit()

def get_all_grades():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT s.name AS student, c.name AS course, g.subcategory, g.score, g.weighted_score
        FROM grades g
        JOIN students s ON s.id = g.student_id
        JOIN courses c ON c.id = g.course_id
        ''')
        return cursor.fetchall()
