from application.dll.db import db
from application.dll.db.document import Document


class User(Document):
    collection = db.users

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.email
