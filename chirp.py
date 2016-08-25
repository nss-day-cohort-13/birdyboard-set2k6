import uuid

class Chirp:

    def __init__(self, message, user_uuid):
        self.message = message
        self.user_uuid = user_uuid
        # self.private = private
        # self.target = receiver
        self.chirp_uuid = uuid.uuid4()


if __name__ == '__main__':
  c = Chirp()
