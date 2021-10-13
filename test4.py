import unittest
class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('set up method')
     
    def testAdd(self): # test method names begin with 'test'
            self.assertEqual((1 + 2), 5)
            print('hai')
   
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
    
    @classmethod
    def tearDownClass(cls):
        print('teardown method')

unittest.main()
#setup,test,tearDown name are fixed