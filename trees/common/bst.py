from common.tree_node import TreeNode

class BinaryTree:
    def __init__(self, root: None):
        self.root: TreeNode = root

    def __insert(self, value: int, current_node: TreeNode):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value=value)
            else:
                self.__insert(value=value, current_node=current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value=value)
            else:
                self.__insert(value=value, current_node=current_node.right)
        else:
            print(f'Value: {value} is already in the tree')

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value=value)
        else:
            self.__insert(value=value, current_node=self.root)

    def __search(self, value: int, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__search(value=value, current_node=current_node.left)
        else:
            return self.__search(value=value, current_node=current_node.right)

    def search(self, value: int):
        if self.root is None:
            print('Tree is empty')
            return False
        else:
            return self.__search(value=value, current_node=self.root)

    def __pre_order(self, current_node: TreeNode, output: list):
        if current_node is not None:
            output.append(current_node.value)
            self.__pre_order(current_node=current_node.left, output=output)
            self.__pre_order(current_node=current_node.right, output=output)
        return output

    def dfs_pre_order(self):
        output = []
        self.__pre_order(self.root, output)
        return output

    def __in_order(self, current_node: TreeNode, output: list):
        if current_node is not None:
            self.__in_order(current_node=current_node.left, output=output)
            output.append(current_node.value)
            self.__in_order(current_node=current_node.right, output=output)
        return output

    def dfs_in_order(self):
        output = []
        self.__in_order(current_node=self.root, output=output)
        return output

    def __post_order(self, current_node: TreeNode, output: list):
        if current_node is not None:
            self.__post_order(current_node=current_node.left, output=output)
            self.__post_order(current_node=current_node.right, output=output)
            output.append(current_node.value)
        return output

    def dfs_post_order(self):
        output = []
        self.__post_order(current_node=self.root, output=output)
        return output
