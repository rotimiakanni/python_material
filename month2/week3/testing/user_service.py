class UserService:
    def get_users_from_db(self):
        return [
            {"username": "johndoe"},
            {"username": "alice"},
        ]


user_service = UserService()
