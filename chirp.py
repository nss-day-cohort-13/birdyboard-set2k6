import uuid

class Chirp:

    def __init__(self, message, user, private, receiver = None):
        self.message = message
        self.user_id = user
        self.private = private
        self.target = receiver
        self.chirp_uuid = uuid.uuid4()


if __name__ == '__main__':
  c = Chirp()
