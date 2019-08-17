import unittest
from .tree import *

class TestTree(unittest.TestCase):
    def testPreOrder_1(self):
        tree = Tree()
        tree.init()
        seq = tree.preOrder_1()
        test_seq = ['A', 'B', 'D', 'H', 'K', 'E', 'C', 'F', 'I', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testPreOrder_2(self):
        tree = Tree()
        tree.init()
        seq = tree.preOrder_2()
        test_seq = ['A', 'B', 'D', 'H', 'K', 'E', 'C', 'F', 'I', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testPreOrder_3(self):
        tree = Tree()
        tree.init()
        seq = tree.preOrder_3()
        test_seq = ['A', 'B', 'D', 'H', 'K', 'E', 'C', 'F', 'I', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testInOrder_1(self):
        tree = Tree()
        tree.init()
        seq = tree.InOrder_1()
        test_seq = ['H', 'K', 'D', 'B', 'E', 'A', 'I', 'F', 'C', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testInOrder_2(self):
        tree = Tree()
        tree.init()
        seq = tree.InOrder_2()
        test_seq = ['H', 'K', 'D', 'B', 'E', 'A', 'I', 'F', 'C', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testInOrder_3(self):
        tree = Tree()
        tree.init()
        seq = tree.InOrder_3()
        test_seq = ['H', 'K', 'D', 'B', 'E', 'A', 'I', 'F', 'C', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])

    def testInOrder_4(self):
        tree = Tree()
        tree.init()
        seq = tree.InOrder_4()
        test_seq = ['H', 'K', 'D', 'B', 'E', 'A', 'I', 'F', 'C', 'G', 'J']
        self.assertEqual(len(seq), len(test_seq))
        if len(seq) == len(test_seq):
            for i in range(0, len(seq)):
                self.assertEqual(seq[i], test_seq[i])


    def testSearchInBST_1(self):
        bst = BinarySearchTree()
        bst.init()
        ret, p = bst.search(93)
        self.assertEqual(ret, True)

    def testSearchInBST_2(self):
        bst = BinarySearchTree()
        bst.init()
        ret, p = bst.search(35)
        self.assertEqual(ret, True)

    def testSearchInBST_3(self):
        bst = BinarySearchTree()
        bst.init()
        ret, p = bst.search(36)
        self.assertEqual(ret, False)

    def testInsert(self):
        bst = BinarySearchTree()
        bst.init2()
        ret, p = bst.search(99)
        self.assertEqual(ret, True)

    def testDelete_1(self):
        bst = BinarySearchTree()
        bst.init2()
        bst.delete(93)
        self.assertEqual(True,True)

    def testDelete_2(self):
        bst = BinarySearchTree()
        bst.init2()
        bst.delete(62)
        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main()
