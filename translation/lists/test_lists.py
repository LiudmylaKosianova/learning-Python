import unittest
import lists


class Test_lists(unittest.TestCase):

    def test_howMany(self):
        self.assertEqual(lists.howMany([], 3), 0)
        self.assertEqual(lists.howMany([3, 3, 3, 3, 3], 3), 5)
        self.assertEqual(lists.howMany([3, 3, 3, 3, 3], 1), 0)
        self.assertEqual(lists.howMany([3, 0, 3, 0, 3], 3), 3)

    def test_findMax(self):
        self.assertEqual(lists.findMax([]), -1)
        self.assertEqual(lists.findMax([1, 3, 5, 7, 9, 1, 2, 3, 4, 5]), 9)
        self.assertEqual(lists.findMax([1, 1, 1, 1, 1]), 1)

    def test_maxList(self):
        self.assertEqual(lists.maxList([]), None)
        self.assertEqual(lists.maxList([1,2,3,1,2,3,1]), [3,3])
        self.assertEqual(lists.maxList([1,2,2,3,1]), [3])

    def test_swapZero(self):
        self.assertEqual(lists.swapZero([1,2,0,3,4,0,5]), [1,2,3,4,5,0,0])
        self.assertEqual(lists.swapZero([0,1,2,0,3,4,0,5]), [1,2,3,4,5,0,0,0])
        self.assertEqual(lists.swapZero([1,2,0,3,4,0,5,0]), [1,2,3,4,5,0,0,0])
        self.assertEqual(lists.swapZero([0,1,2,0,3,4,0,5,0]), [1,2,3,4,5,0,0,0,0])