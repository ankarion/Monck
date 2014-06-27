from Monck import Monck
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        #initialising Monck for tests
        self.monck = Monck()

    #Should allways return Monck object
    def test_getitem(self):
        #__getitem__ should return Monck object
        self.assertIsInstance(self.monck[1], Monck)

    def test_call(self):
        #call should return Monck object
        self.assertIsInstance(self.monck(), Monck)

    #test saving values of Monck object
    def test_call_id(self):
        #call should return different Monck object
        self.assertNotEqual(self.monck(), self.monck)
        self.assertNotEqual(self.monck()()()(),self.monck())
        #but sometimes it should return the same Monck object
        self.assertEqual(self.monck(), self.monck())

    def test_getitem_id(self):
        #getitem should return different Monck object
        self.assertNotEqual(self.monck[1], self.monck)
        self.assertNotEqual(self.monck['1'], self.monck)
        self.assertNotEqual(self.monck['1'], self.monck[1])
        #but sometimes it should return the same Monck object
        self.assertEqual(self.monck[1], self.monck[1])

    def test_atribute(self):
        #calling atribute should return Monck object
        self.assertIsInstance(self.monck.anything, Monck)
        #and save the value
        self.monck.pi = 0
        self.assertEqual(self.monck.pi,0)

if __name__=="__main__":
    unittest.main()
