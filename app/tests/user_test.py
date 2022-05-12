import unittest
from models import user

User=user.User

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(1234,'ronval','Valarierono97@gmail.com','15502','Are you a bank loan?Because you have my interest','This is great!')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))


if __name__ == '__main__':
    unittest.main()