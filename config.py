import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Gives access to the project in ANY OS we find ourselves in
# Allows outside files/folders to be added to the project from the base directory)

class Config:
    """
    Sets configuration variables for our Flask app
    Eventually will use hidden variable items, but for now
    we'll leave them exposed in Config
    """
    SECRET_KEY = "In a hole in the ground..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
# To connect with SQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False