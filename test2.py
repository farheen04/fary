import unittest
class Demo(unittest.TestCase):
    def setUp(self):
        print('setup execution')
    
    def test(self):
        print('test method')

    def test_1(self):
        print('test method 2')
    
    def tearDown(self):
        print('teardown method')

unittest.main()
#if two test method are executed then setup and teardown executed two times
