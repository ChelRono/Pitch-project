import unittest
from models import pitch

Pitch=pitch.Pitch

class PitchesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1234,'Pickup lines','Are you a bank loan?Because you have my interest','2020-12-5','This is great!')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()