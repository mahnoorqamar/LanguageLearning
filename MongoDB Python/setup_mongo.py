from pymongo import MongoClient
import config

def main():
    uri = config.MONGODB_CONNECTION_STRING
    client = MongoClient(uri)

    db = client.language_learning

    db.Languages.drop()
    db.Courses.drop()
    db.Students.drop()
    db.Enrollments.drop()

    languages_collection = db.Languages
    courses_collection = db.Courses
    students_collection = db.Students
    enrollments_collection = db.Enrollments

    languages = [
        { "_id": 1, "name": "Hindi" }, { "_id": 2, "name": "English" },
        { "_id": 3, "name": "Urdu" }, { "_id": 4, "name": "French" },
        { "_id": 5, "name": "Spanish" }, { "_id": 6, "name": "Korean" },
        { "_id": 7, "name": "Chinese" }, { "_id": 8, "name": "Japanese" },
        { "_id": 9, "name": "Arabic" }, { "_id": 10, "name": "Bengali" },
        { "_id": 11, "name": "German" }, { "_id": 12, "name": "Italian" },
        { "_id": 13, "name": "Russian" }, { "_id": 14, "name": "Portuguese" },
        { "_id": 15, "name": "Dutch" }
    ]
    languages_collection.insert_many(languages)

    courses = [
        { "_id": 1, "name": "Basic Hindi", "language_id": 1 },
        { "_id": 2, "name": "Advanced Hindi", "language_id": 1 },
        { "_id": 3, "name": "Basic English", "language_id": 2 },
        { "_id": 4, "name": "Advanced English", "language_id": 2 },
        { "_id": 5, "name": "Basic Urdu", "language_id": 3 },
        { "_id": 6, "name": "Advanced Urdu", "language_id": 3 },
        { "_id": 7, "name": "Basic French", "language_id": 4 },
        { "_id": 8, "name": "Advanced French", "language_id": 4 },
        { "_id": 9, "name": "Basic Spanish", "language_id": 5 },
        { "_id": 10, "name": "Advanced Spanish", "language_id": 5 },
        { "_id": 11, "name": "Basic Korean", "language_id": 6 },
        { "_id": 12, "name": "Advanced Korean", "language_id": 6 },
        { "_id": 13, "name": "Basic Chinese", "language_id": 7 },
        { "_id": 14, "name": "Advanced Chinese", "language_id": 7 },
        { "_id": 15, "name": "Basic Japanese", "language_id": 8 },
        { "_id": 16, "name": "Advanced Japanese", "language_id": 8 },
        { "_id": 17, "name": "Basic Arabic", "language_id": 9 },
        { "_id": 18, "name": "Advanced Arabic", "language_id": 9 }
    ]
    courses_collection.insert_many(courses)

    students = [
        { "_id": 1, "name": "Mahnoor", "age": 21 }, { "_id": 2, "name": "Sakshi", "age": 22 },
        { "_id": 3, "name": "Preeti", "age": 23 }, { "_id": 4, "name": "Anjali", "age": 24 },
        { "_id": 5, "name": "Deepali", "age": 25 }, { "_id": 6, "name": "Neha", "age": 26 },
        { "_id": 7, "name": "Nikita", "age": 27 }, { "_id": 8, "name": "Hema", "age": 28 },
        { "_id": 9, "name": "Pooja", "age": 29 }, { "_id": 10, "name": "Disha", "age": 30 },
        { "_id": 11, "name": "Farah", "age": 31 }, { "_id": 12, "name": "Khushi", "age": 32 },
        { "_id": 13, "name": "Vinita", "age": 33 }, { "_id": 14, "name": "Shweta", "age": 34 },
        { "_id": 15, "name": "Shallu", "age": 35 }
    ]
    students_collection.insert_many(students)

    enrollments = [
        { "_id": 1, "student_id": 1, "course_id": 1 },
        { "_id": 2, "student_id": 1, "course_id": 3 },
        { "_id": 3, "student_id": 2, "course_id": 1 },
        { "_id": 4, "student_id": 2, "course_id": 4 },
        { "_id": 5, "student_id": 3, "course_id": 5 },
        { "_id": 6, "student_id": 4, "course_id": 6 },
        { "_id": 7, "student_id": 5, "course_id": 7 },
        { "_id": 8, "student_id": 6, "course_id": 8 },
        { "_id": 9, "student_id": 7, "course_id": 9 },
        { "_id": 10, "student_id": 8, "course_id": 10 },
        { "_id": 11, "student_id": 9, "course_id": 11 },
        { "_id": 12, "student_id": 10, "course_id": 12 },
        { "_id": 13, "student_id": 11, "course_id": 13 },
        { "_id": 14, "student_id": 12, "course_id": 14 },
        { "_id": 15, "student_id": 13, "course_id": 15 }
    ]
    enrollments_collection.insert_many(enrollments)

    print("Data inserted successfully!")

if __name__ == "__main__":
    main()
