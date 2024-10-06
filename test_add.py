import unittest

from add import additem, unify
from checkConstraints import checkBOD, checkSOD


class MyTestCase(unittest.TestCase):

    def test_additem_three(self):
        lst = [["a", "b", "c"]]
        item = "d"
        result = additem(lst, item)
        expected = [[['a', 'b', 'c', 'd']], [['a', 'b', 'c'], ['d']]]
        self.assertEqual(result, expected, "Test case failed for a list with one sublist")

    def test_additem_five(self):
        result = additem([["a", "b"], ["c"], ["d", "e"]], "f")
        expected = [[['a', 'b', 'f'], ['c'], ['d', 'e']], [['a', 'b'], ['c', 'f'], ['d', 'e']],
                    [['a', 'b'], ['c'], ['d', 'e', 'f']], [['a', 'b'], ['c'], ['d', 'e'], ['f']]]
        self.assertEqual(result, expected, "Test case failed for a list with one sublist")

    def test_bod(self):
        result = checkBOD("A", "B", [["A", "B"], ["C"]])
        self.assertTrue(result, "BOD failed")

    def test_not_bod(self):
        result = checkBOD("A", "B", [["A"], ["B", "C"]])
        self.assertFalse(result, "BOD failed")

    def test_sod(self):
        result = checkSOD("A", "B", [["A", "B"], ["C"]])
        self.assertFalse(result, "BOD failed")

    def test_not_sod(self):
        result = checkSOD("A", "B", [["A"], ["B", "C"]])
        self.assertTrue(result, "BOD failed")

    def test_unify(self):
        result = [[0], [1, 2], [3], [4], [5, 6, 7]]
        self.assertEqual(result, unify([[1, 2], [6, 7], [6, 5]], 8), "Union find not working")

    def test_not_unify(self):
        result = [[0], [1, 2], [4], [3, 5], [6, 7], [8], [9], [10]]
        self.assertEqual(result, unify([[1, 2], [6, 7], [3, 5]], 11), "Union find not working")


if __name__ == '__main__':
    unittest.main()
