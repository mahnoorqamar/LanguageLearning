from pymongo import MongoClient
import config


def main():
    client = MongoClient(config.MONGODB_CONNECTION_STRING)
    db = client.language_learning

    collections = ["Languages", "Courses", "Students", "Enrollments"]

    for collection_name in collections:
        collection = db[collection_name]
        count = collection.count_documents({})
        sample_docs = list(collection.find().limit(3))

        print(f"Collection: {collection_name}")
        print(f"Count of rows: {count}")
        print("Sample documents:")
        for doc in sample_docs:
            print(doc)
        print("-" * 50)

    print("Joining Courses and Languages collections:")
    pipeline = [
        {
            "$lookup": {
                "from": "Languages",
                "localField": "language_id",
                "foreignField": "_id",
                "as": "language"
            }
        },
        {
            "$unwind": "$language"
        },
        {
            "$project": {
                "course_name": "$name",
                "language_name": "$language.name"
            }
        },
        {
            "$limit": 10
        }
    ]

    joined_data = db.Courses.aggregate(pipeline)

    for doc in joined_data:
        print(doc)


if __name__ == "__main__":
    main()
