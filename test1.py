import unittest
class Demo(unittest.TestCase):
    
    def setUp(self):
        print('setup execution')
    
    def testin(self):
        print('test method')
    
    def tearDown(self):
        print('teardown method')

unittest.main()
#setup,test,tearDown name are fixed
