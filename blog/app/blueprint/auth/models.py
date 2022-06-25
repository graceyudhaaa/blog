from ...extensions import bcrypt

# usermixin pymongo don't neccesary


class User:
    def __init__(self, _id, username, email, avatar):
        self._id = _id
        self.username = username
        self.email = email
        self.avatar = avatar

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)
