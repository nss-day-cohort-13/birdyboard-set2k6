import unittest
import user

class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    newUser = user.User("Tractor Ryan", "tryan")

    self.assertEqual("Tractor Ryan", newUser.full_name)
    self.assertEqual("tryan", newUser.screen_name)
    self.assertIsNotNone(newUser.user_id)
    self.assertIsInstance(newUser, user.User)
    pass



if __name__ == '__main__':
    unittest.main()
