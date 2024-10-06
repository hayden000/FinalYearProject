import unittest

from counting import checkAllCounting, atMost, atLeast


class MyTestCase(unittest.TestCase):
    def test_something(self):
        jobGroups = [[1, 2], [3], [4, 5]]
        atMostCounts = [3, 4]
        atMostLists = [[1, 2, 3], [2, 3]]
        atLeastCounts = [1, 2]
        atLeastLists = [[4], [4, 5]]
        self.assertFalse(checkAllCounting(jobGroups, atMostCounts, atMostLists, atLeastCounts, atLeastLists))

    def test_atMost(self):
        jobGroups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        atMostCount = 2
        atMostList = [1, 4, 7]
        self.assertFalse(atMost(jobGroups, atMostCount, atMostList))

    def test_atLeast(self):
        jobGroups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        atLeastCount = 2
        atLeastList = [1, 4, 7]
        self.assertTrue(atLeast(jobGroups, atLeastCount, atLeastList))


if __name__ == '__main__':
    unittest.main()
