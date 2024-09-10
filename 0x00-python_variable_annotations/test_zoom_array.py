import unittest
from typing import List, Tuple
from 102_type_checking import zoom_array

class TestZoomArray(unittest.TestCase):
    
    def test_zoom_array_default_factor(self):
        array = (12, 72, 91)
        result = zoom_array(array)
        expected = [12, 12, 72, 72, 91, 91]
        self.assertEqual(result, expected)
    
    def test_zoom_array_custom_factor(self):
        array = (12, 72, 91)
        result = zoom_array(array, 3)
        expected = [12, 12, 12, 72, 72, 72, 91, 91, 91]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
