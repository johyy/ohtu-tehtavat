from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        correct_password = False

        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if len(username) < 3:
            raise UserInputError("Invalid username")

        if len(password) < 8:
            raise UserInputError("Invalid password")
        
        for letter in password:
            if letter in "0123456789":
                correct_password = True
        
        if correct_password == False:
            raise UserInputError("Invalid password")