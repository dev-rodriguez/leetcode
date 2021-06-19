from common.tree_node import TreeNode
from common.bst import BinaryTree

root = TreeNode(value=1)
bst = BinaryTree(root=root)

print('root', bst.root.value)
print('left child', bst.root.left)
print('right child', bst.root.right)

print(bst.search(1))

bst.insert(3)
bst.insert(6)
bst.insert(2)
bst.insert(1)

print(bst.search(2))