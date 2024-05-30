import mysql.connector
from config import db_config

connection = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)
cursor = connection.cursor()

def query_database():
    tables = ['Languages', 'Courses', 'Students', 'Enrollments']

    for table in tables:
        # Count of rows
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"Table: {table}, Count: {count}")

        # Sample of 3 rows
        cursor.execute(f"SELECT * FROM {table} LIMIT 3")
        sample_rows = cursor.fetchall()
        print(f"Sample rows from {table}:")
        for row in sample_rows:
            print(row)
        print()

    # Join operation (example: joining Students and Enrollments tables)
    cursor.execute("""
        SELECT Students.name AS Student_Name, Students.age AS Student_Age, Courses.name AS Course_Name
        FROM Students
        INNER JOIN Enrollments ON Students.id = Enrollments.student_id
        INNER JOIN Courses ON Enrollments.course_id = Courses.id
        LIMIT 5
    """)
    join_result = cursor.fetchall()
    print("Joining Students, Enrollments, and Courses tables:")
    for row in join_result:
        print(row)

query_database()

connection.close()


