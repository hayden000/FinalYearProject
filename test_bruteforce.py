import unittest

from generatePartitions import generate_partitions


class MyTestCase(unittest.TestCase):
    def test_generate_all(self):
        result = [[[1], [2], [3], [4]], [[1, 2], [3], [4]], [[2], [1, 3], [4]], [[2], [3], [1, 4]], [[1], [2, 3], [4]],
                  [[1, 2, 3], [4]], [[2, 3], [1, 4]], [[1], [3], [2, 4]], [[1, 3], [2, 4]], [[3], [1, 2, 4]],
                  [[1], [2], [3, 4]], [[1, 2], [3, 4]], [[2], [1, 3, 4]], [[1], [2, 3, 4]], [[1, 2, 3, 4]]]
        self.assertEqual(generate_partitions(4), result, "generate does not work")  # add assertion here

    def test_generate_one(self):
        result = [[[1]]]
        self.assertEqual(generate_partitions(1), result, "generate does not work")  # add assertion here


if __name__ == '__main__':
    unittest.main()
