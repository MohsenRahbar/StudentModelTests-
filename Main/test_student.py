import unittest
from student import student


class teststudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("SetupClass")
    
    @classmethod
    def tearDownClass(cls) :
        print("TearDown")
    
    def setUp(self) :
        self.firststudent = student("Mohsen","Rahbar",0.0)
        self.secondstudent = student("Ali","Xzadh", 0.0)
    
    def tearDown(self) :
        pass
    
    def testmaill(self) :
        self.assertEqual(self.firststudent.maill(),"Mohsen.Rahbar@tu.io.com")
        self.assertEqual(self.secondstudent.maill(),"Ali.Xzadh@tu.io.com")
        
    def test_full_name(self) :
        self.assertEqual(self.firststudent.full_name() , "Mohsen Rahbar")
        self.assertEqual(self.secondstudent.full_name() , "Ali Xzadh")
        
    def inc_mark(self) : 
        self.firststudent.inc_mark()
        self.secondstudent.inc_mark()
        self.secondstudent.inc_mark()
        
        self.assertEqual(self.firststudent.mark,0.5)
        self.assertEqual(self.secondstudent.mark,1.0)
        
if __name__ : 
    unittest.main()
