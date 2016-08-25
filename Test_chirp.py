import unittest
from user import *
from chirp import *
# import CoversationSingleton


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_reply_public_chirp_creation(self):
    pass


  def test_new_public_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_uuid,
                  private=False
                  )

    # it_exists = CoversationSingleton.chirp_exists_in_conversation(chirp)

    # self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "Hi everyone")
    self.assertEqual(chirp.user_uuid, source.user_uuid)
    # self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_uuid)


  def test_private_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    target = User("George Lucas", "hahajarjar")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_uuid,
                  private=True,
                  receiver=target.user_uuid
                  )
    self.assertIsInstance(chirp, Chirp)




if __name__ == '__main__':
    unittest.main()
