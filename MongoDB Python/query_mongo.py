# query_mongo.py

from pymongo import MongoClient
import config  # Import the config file

def find_courses_for_language(language_name):
    uri = config.MONGODB_CONNECTION_STRING  # Use the connection string from config.py
    client = MongoClient(uri)
    db = client.language_learning

    languages_collection = db.Languages
    courses_collection = db.Courses

    language = languages_collection.find_one({ "name": language_name })
    if language:
        courses = courses_collection.find({ "language_id": language["_id"] })
        return list(courses)
    return []

def find_students_in_course(course_name):
    uri = config.MONGODB_CONNECTION_STRING  # Use the connection string from config.py
    client = MongoClient(uri)
    db = client.language_learning

    courses_collection = db.Courses
    enrollments_collection = db.Enrollments
    students_collection = db.Students

    course = courses_collection.find_one({ "name": course_name })
    if course:
        enrollments = enrollments_collection.find({ "course_id": course["_id"] })
        student_ids = [enrollment["student_id"] for enrollment in enrollments]
        students = students_collection.find({ "_id": { "$in": student_ids } })
        return list(students)
    return []

def find_courses_for_student(student_name):
    uri = config.MONGODB_CONNECTION_STRING  # Use the connection string from config.py
    client = MongoClient(uri)
    db = client.language_learning

    students_collection = db.Students
    enrollments_collection = db.Enrollments
    courses_collection = db.Courses

    student = students_collection.find_one({ "name": student_name })
    if student:
        enrollments = enrollments_collection.find({ "student_id": student["_id"] })
        course_ids = [enrollment["course_id"] for enrollment in enrollments]
        courses = courses_collection.find({ "_id": { "$in": course_ids } })
        return list(courses)
    return []

if __name__ == "__main__":
    # Test the functions
    hindi_courses = find_courses_for_language("Hindi")
    print("Hindi Courses:", hindi_courses)

    students_in_basic_hindi = find_students_in_course("Basic Hindi")
    print("Students in Basic Hindi:", students_in_basic_hindi)

    courses_for_mahnoor = find_courses_for_student("Mahnoor")
    print("Courses for Mahnoor:", courses_for_mahnoor)
