import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class for user class
    '''
#Start user tests
    def setUp(self):
        '''
        test to run before each test cases
        '''

        self.new_credentials = Credentials("Twitter", "32667842")
        self.new_user = User("Peter", "pet", "Pete")

    def test_init(self):
            '''
            test_init for testing object initialization
            '''

            self.assertEqual(self.new_credentials.account_name, "Twitter")

            self.assertEqual(self.new_credentials.password, "32667842")

            self.assertEqual(self.new_user.first_name, "Peter")

            self.assertEqual(self.new_user.last_name, "pet")

            self.assertEqual(self.new_user.username, "Pete")


if __name__== '__main__':
    unittest.main()