import unittest

import ortool


class MyTestCase(unittest.TestCase):
    def test_SAT(self):
        rules = [(1, 2, "BOD"), (2, 3, "SOD"), (3, 4, "SOD")]
        auths = [[3], [2, 4], [1], [2, 3, 4]]
        SATsolver = ortool.SATsolver(rules, auths)
        print(SATsolver)
        # authsself.assertEqual(SATsolver, [[2, 3], [3, 3], [4, 1], [5, 3]], "SAT solver not working")


if __name__ == '__main__':
    unittest.main()
