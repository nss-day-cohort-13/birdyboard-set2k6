import uuid

class User:


    def __init__(self, fullname, username):
        self.screen_name = username
        self.full_name = fullname
        self.user_uuid = uuid.uuid4()


if __name__ == '__main__':
  u = User()

