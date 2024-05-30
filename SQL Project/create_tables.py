import mysql.connector
from config import db_config

connection = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password']
)
cursor = connection.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
cursor.execute(f"USE {db_config['database']}")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Languages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        language_id INT,
        FOREIGN KEY (language_id) REFERENCES Languages(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        course_id INT,
        FOREIGN KEY (student_id) REFERENCES Students(id),
        FOREIGN KEY (course_id) REFERENCES Courses(id)
    )
""")

languages = [
    ('Hindi',), ('English',), ('Urdu',), ('French',), ('Spanish',),
    ('Korean',), ('Chinese',), ('Japanese',), ('Arabic',), ('Bengali',),
    ('German',), ('Italian',), ('Russian',), ('Portuguese',), ('Dutch',)
]
cursor.executemany("INSERT INTO Languages (name) VALUES (%s)", languages)

courses = [
    ('Basic Hindi', 1), ('Advanced Hindi', 1),
    ('Basic English', 2), ('Advanced English', 2),
    ('Basic Urdu', 3), ('Advanced Urdu', 3),
    ('Basic French', 4), ('Advanced French', 4),
    ('Basic Spanish', 5), ('Advanced Spanish', 5),
    ('Basic Korean', 6), ('Advanced Korean', 6),
    ('Basic Chinese', 7), ('Advanced Chinese', 7),
    ('Basic Japanese', 8), ('Advanced Japanese', 8),
    ('Basic Arabic', 9), ('Advanced Arabic', 9)
]
cursor.executemany("INSERT INTO Courses (name, language_id) VALUES (%s, %s)", courses)
students = [
    ('Alice', 21), ('Bob', 22), ('Charlie', 23), ('David', 24), ('Eva', 25),
    ('Frank', 26), ('Grace', 27), ('Heidi', 28), ('Ivan', 29), ('Judy', 30),
    ('Mallory', 31), ('Niaj', 32), ('Oscar', 33), ('Peggy', 34), ('Sybil', 35)
]
cursor.executemany("INSERT INTO Students (name, age) VALUES (%s, %s)", students)

enrollments = [
    (1, 1), (1, 3), (2, 1), (2, 4), (3, 5),
    (4, 6), (5, 7), (6, 8), (7, 9), (8, 10),
    (9, 11), (10, 12), (11, 13), (12, 14), (13, 15)
]
cursor.executemany("INSERT INTO Enrollments (student_id, course_id) VALUES (%s, %s)", enrollments)
connection.commit()
connection.close()
