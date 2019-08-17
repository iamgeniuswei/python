class TreeNode(object):
    """
    Define a node in the Binary Tree
    """

    def __init__(self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None
        # Add the below to implement Tree::InOrder_4()
        self.parent = None
        # end

    def insertAsLChild(self, data = None):
        lchild = TreeNode(data)
        self.lchild = lchild
        # Add the below to implement Tree::InOrder_4()
        lchild.parent = self
        # end
        return lchild

    def insertAsRChild(self, data = None):
        rchild = TreeNode(data)
        self.rchild = rchild
        # Add the below to implement Tree::InOrder_4()
        rchild.parent = self
        # end
        return rchild

    def succ(self):
        node = self
        if self.rchild is not None:
            node = self.rchild
            while node.lchild is not None:
                node = node.lchild
        else:
            while node.isRChild():
                node = node.parent
            node = node.parent
        return node

    def isRChild(self):
        if self.parent is not None:
            if self.parent.rchild == self:
                return True
            return False
        return False

class Tree(object):
    """
    Define a Binary Tree
    """

    def __init__(self):
        self.numNode = 0
        self.root = None

    def __insertAsRoot(self, data):
        self.root = TreeNode(data)

    def init(self):
        self.__insertAsRoot('A')
        B = self.root.insertAsLChild('B')
        C = self.root.insertAsRChild('C')
        D = B.insertAsLChild('D')
        E = B.insertAsRChild('E')
        H = D.insertAsLChild('H')
        K = H.insertAsRChild('K')
        F = C.insertAsLChild('F')
        G = C.insertAsRChild('G')
        I = F.insertAsLChild('I')
        J = G.insertAsRChild('J')

    def preOrder_1(self):
        seq = []
        self.__preOrder_1(self.root, seq)
        return seq

    def preOrder_2(self):
        seq =[]
        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            item = stack.pop()
            seq.append(item.data)
            if item.rchild is not None:
                stack.append(item.rchild)
            if item.lchild is not None:
                stack.append(item.lchild)
        return seq

    def preOrder_3(self):
        seq = []
        stack = []
        start = self.root
        while True:
            self.__goAlongAndVisitLeft(start, stack, seq)
            if len(stack) == 0:
                break
            start = stack.pop()
        return seq

    def __goAlongAndVisitLeft(self, node, stack, seq):
        while node is not None:
            seq.append(node.data)
            stack.append(node.rchild)
            node = node.lchild


    def __preOrder_1(self, node, seq):
        if node is None:
            return
        seq.append(node.data)
        self.__preOrder_1(node.lchild, seq)
        self.__preOrder_1(node.rchild, seq)


    def InOrder_1(self):
        seq = []
        self.__inOrder_R(self.root, seq)
        return seq


    def InOrder_2(self):
        seq = []
        stack = []
        start = self.root
        while True:
            self.__goAlongLeft(start, stack)
            if len(stack) == 0:
                break
            start = stack.pop()
            seq.append(start.data)
            start = start.rchild
        return seq

    def InOrder_3(self):
        seq = []
        stack = []
        start = self.root
        while True:
            if start is not None:
                stack.append(start)
                start = start.lchild
            elif len(stack) > 0:
                start = stack.pop()
                seq.append(start.data)
                start = start.rchild
            else:
                break
        return seq

    def InOrder_4(self):
        seq = []
        backTrack = False
        start = self.root
        while True:
            if backTrack is not True and start.lchild is not None:
                start = start.lchild
            else:
                seq.append(start.data)
                if start.rchild is not None:
                    start = start.rchild
                    backTrack = False
                else:
                    start = start.succ()
                    if start is None:
                        break
                    backTrack = True
        return seq




    def __goAlongLeft(self, node, stack):
        while node is not None:
            stack.append(node)
            node = node.lchild


    def __inOrder_R(self, node, seq):
        if node is None:
            return None
        self.__inOrder_R(node.lchild, seq)
        seq.append(node.data)
        self.__inOrder_R(node.rchild, seq)


class BinarySearchTree(Tree):
    """
    Define a binary search Tree
    """
    def init(self):
        self.root = TreeNode(62)
        A = self.root.insertAsLChild(58)
        B = self.root.insertAsRChild(88)
        C = A.insertAsLChild(47)
        D = C.insertAsLChild(35)
        E = C.insertAsRChild(51)
        F = D.insertAsRChild(37)
        G = B.insertAsLChild(73)
        H = B.insertAsRChild(99)
        I = H.insertAsLChild(93)

    def init2(self):
        self.root = TreeNode(62)
        self.insert(58)
        self.insert(88)
        self.insert(47)
        self.insert(35)
        self.insert(51)
        self.insert(37)
        self.insert(73)
        self.insert(99)
        self.insert(93)


    def insert(self, key):
        ret, p = self.search(key)
        if ret:
            return p
        else:
            if p.data > key:
                node = p.insertAsLChild(key)
            else:
                node = p.insertAsRChild(key)
            return node

    def delete(self, key):
        ret, p = self.search(key)
        if ret is not True:
            return False
        if p.lchild is None or p.rchild is None:
            parent = p.parent
            child = None
            if p.lchild is not None:
                child = p.lchild
            else:
                child = p.rchild
            if p.isRChild():
                parent.rchild = child
            else:
                parent.lchild = child
        else:
            succ = p.succ()
            temp = p.data
            p.data = succ.data
            self.delete(temp)
        return p

    def search(self, key):
        start = self.root
        while start is not None:
            p = start
            if start.data == key:
                return True, p
            elif start.data > key:
                start = start.lchild
            else:
                start = start.rchild
        return False, p

