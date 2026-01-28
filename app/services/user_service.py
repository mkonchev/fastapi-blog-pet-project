class UserService:

    def get_current_user(self):
        """
        сделать jwt проверку
        """
        return {
            "user_id": 1,
            "username": "admin",
            "role": "admin"
        }

    def is_admin(self, user: dict) -> bool:
        return user.get("role") == "admin"

    def validate_user_access(self, user: dict) -> None:
        if not self.is_admin(user):
            raise PermissionError("User is not admin")
