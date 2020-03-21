import unittest as ut
import numpy as np


class ExampleTests(ut.TestCase):
    # All tests need to be run in a class
    
    def setUp(self):
        # setUp and tearDown are special
        self.a = 3
        self.pi = 3.1415926535
    
    def tearDown(self):
        pass
    
    # Simple ways to do tests here
    def test_a_equals_3(self):
        self.assertEqual(self.a, 3)
    
    def test_a_lt_pi(self):
        self.assertTrue(self.a < self.pi)
    
    def test_pi_approx(self):
        # Only works on floats!
        self.assertAlmostEqual(self.pi, 355/113, places=5)
        
    def test_3_approx(self):
        np.testing.assert_almost_equal(self.a, 3.000000001)
    
    def test_raises_error(self):
        with self.assertRaises(ValueError):
            raise ValueError


if __name__ == '__main__':
    # Run the tests
    ut.main(verbosity=2)
