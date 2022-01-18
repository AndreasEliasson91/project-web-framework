from pymongo import MongoClient
import gridfs

client = None
db = None
fs = None


def init_db(app):
    """
    Set environment variables for the database in ..env file in the project root
    folder.
    :param app: Flask app object
    :return: None
    """
    global client, db, fs
    username = app.config['DB_USER']
    password = app.config['DB_PASSWORD']
    host = app.config['DB_HOST']
    port = int(app.config['DB_PORT'])
    database = app.config['DB_NAME']
    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
    db = client[database]
    fs = gridfs.GridFS(db)


    #
    # file = 'C:/Users/andre/OneDrive/Skrivbord/father2.png'
    #
    # with open(file, 'rb') as f:
    #     contents = f.read()
    #
    # fs.put(contents, filename='father_2')

    # client.LearningByGames_DB.command(
    #     'createUser', username,
    #     pwd=password,
    #     roles=[{'role': 'readWrite', 'db': database}]
    # )
