from hashlib import md5


class KeyFactory:

    @staticmethod
    def user(user_id: int, user_name: str):
        return {
            'PK': user_id,
            'SK': user_name
        }

