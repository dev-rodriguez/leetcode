from common.tree_node import TreeNode
from common.bst import BinaryTree

root = TreeNode(value=5)
bst = BinaryTree(root=root)

bst.insert(3)
bst.insert(6)
bst.insert(2)
bst.insert(4)
bst.insert(7)

"""
                5
            /       \
          3           6
        /    \      /    \
       2      4           7
"""
print(f'Is value: 2 in the tree:', bst.search(2))
print(f'Is value: 0 in the tree:', bst.search(9))
print('Pre order', bst.dfs_pre_order())
print('In order', bst.dfs_in_order())
print('Post order', bst.dfs_post_order())
