import unittest
class momenta(unittest.TestCase):
    def setUp(self):
        print('用例{}开始执行'.format())
    def tearDown(self):
        print('用例{}执行完了'.format())
    @classmethod
    def setUpClass(cls):
        print('start')
    @classmethod
    def tearDownClass(cls):
        print('off')
    def test_01(self):
        a=[7,8,'ww']
        b=[7,8,'ww']
        self.assertEqual(a,b)
    def test_02(self):
        s={'曹':'永顺','张':'兴慧'}
        y=s['曹']
        self.assertEqual(s,y)
if __name__=='__main__':
    unittest.main()