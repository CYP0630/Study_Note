class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(8)
    node_2 = TreeNode(3)
    node_3 = TreeNode(10)
    node_4 = TreeNode(1)
    node_5 = TreeNode(6)
    node_6 = TreeNode(14)
    node_7 = TreeNode(4)
    node_8 = TreeNode(7)
    node_9 = TreeNode(13)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    node_5.left = node_7
    node_5.right = node_8

    node_6.left = node_9
    
    return node_1

def traverse_tree(root):
    if root is None:
        return 
    print(root.val, end=' ')
    traverse_tree(root.left)
    traverse_tree(root.right)

def inorder_treverse(root):
    if root is None:
        return
    inorder_treverse(root.left)
    print(root.val, end= ' ')
    inorder_treverse(root.right)

def postorder_treverse(root):
    if root is None:
        return
    inorder_treverse(root.left)
    inorder_treverse(root.right)
    print(root.val, end=' ')


root = build_tree()
traverse_tree(root)


