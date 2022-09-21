import unittest, myCalc

class TestCalcMethods(unittest.TestCase):

    def test_costCalc(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual([[0, 1, 1, 0], [0, 62.98, 28.98, 0]], 
        myCalc.costCalc(20))
    
    
    if __name__ == "__main__":
        unittest.main()