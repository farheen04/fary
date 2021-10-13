import unittest
class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class method')
    
    def test(self):
        print('test method')

    def test_1(self):
        print('test method 2')
    
    @classmethod
    def tearDownClass(cls):
        print('teardown method')

unittest.main()
#if settup and teardown are class method  then it will execute only once