import os
from ...extensions import bcrypt
from dotenv import load_dotenv

load_dotenv()

# usermixin pymongo don't neccesary


class User:
    def __init__(self, _id, username, email, avatar):
        self._id = _id
        self.username = username
        self.email = email
        self.avatar = avatar

        if self._id == os.environ["ADMIN_ID"]:
            self.role = "admin"
        else:
            self.role = "user"

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id  # this is for the user_loader parameter

    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)
