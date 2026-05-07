import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from physics import calculate_acceleration

class TestPhysics(unittest.TestCase):
    def test_acceleration_positive(self):
        accel = calculate_acceleration(1000.0, 0.0, 1000.0, 0.5, 0.01)
        # Net Force = 1000 - (0.01 * 1000 * 9.81) = 1000 - 98.1 = 901.9
        # Accel = 0.9019
        self.assertAlmostEqual(accel, 0.9019, places=4)

    def test_acceleration_with_drag(self):
        accel = calculate_acceleration(1000.0, 10.0, 1000.0, 0.5, 0.01)
        # drag = 0.5 * 100 = 50
        # fric = 98.1
        # Net = 1000 - 148.1 = 851.9
        # Accel = 0.8519
        self.assertAlmostEqual(accel, 0.8519, places=4)

if __name__ == "__main__":
    unittest.main()
