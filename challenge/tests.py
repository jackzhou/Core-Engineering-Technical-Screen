import unittest
from sort import sort, REJECTED, SPECIAL, STANDARD


class TestSort(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(50, 40, 30, 10), STANDARD)

    def test_bulky_only(self):
        self.assertEqual(sort(200, 30, 30, 10), SPECIAL)

    def test_heavy_only(self):
        self.assertEqual(sort(50, 40, 30, 20), SPECIAL)

    def test_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 25), REJECTED)

    def test_edge_volume_exact_threshold(self):
        self.assertEqual(sort(100, 100, 100, 10), SPECIAL)

    def test_edge_dimension_exact_threshold(self):
        self.assertEqual(sort(150, 10, 10, 10), SPECIAL)

    def test_edge_mass_exact_threshold(self):
        self.assertEqual(sort(10, 10, 10, 20), SPECIAL)

    def test_width_must_be_positive(self):
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 10)
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)

    def test_height_must_be_positive(self):
        with self.assertRaises(ValueError):
            sort(10, 0, 10, 10)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)

    def test_length_must_be_positive(self):
        with self.assertRaises(ValueError):
            sort(10, 10, 0, 10)
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 10)

    def test_mass_must_be_positive(self):
        with self.assertRaises(ValueError):
            sort(10, 10, 10, 0)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)


if __name__ == "__main__":
    unittest.main()