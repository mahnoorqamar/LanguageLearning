from urllib.parse import quote_plus

username = "mahnoorqamar"
password = "mirak@17"

encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

MONGODB_CONNECTION_STRING = (
    f"mongodb+srv://{encoded_username}:{encoded_password}@cluster17.qqhi58o.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Cluster17"
)


