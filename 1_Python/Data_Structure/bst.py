
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.__root = None

    def add(self, val):
        self.__root = self.__add_helper(self.__root, val)


    def __add_helper(self, root, val):
        if not root:
            return TreeNode(val)


        if root.val > val:
            root.left = self.__add_helper(root.left, val)
        else:
            root.right = self.__add_helper(root.right, val)
        return root

    def contains(self, val):
        return self.__contains_helper(self.__root, val)

    def __contains_helper(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif root.val > val:
            return self.__contains_helper(root.left, val)
        else:
            return self.__contains_helper(root.right, val)


bst = BST()
bst.add(10)
bst.add(11)
bst.add(9)

print(bst.contains(8))

