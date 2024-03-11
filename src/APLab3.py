class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode, depth=0) -> int:

    if root is None:
        return 0

    left_depth = sum_of_depths(root.left, depth + 1)
    right_depth = sum_of_depths(root.right, depth + 1)
    general_depth = left_depth + right_depth + depth

    return general_depth
