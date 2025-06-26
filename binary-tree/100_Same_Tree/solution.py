from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical in structure and node values.

    :param p: Root node of the first binary tree
    :param q: Root node of the second binary tree
    :return: True if trees are identical, False otherwise
    """
    if p is None and q is None:
        return True
    elif isinstance(p, int) and isinstance(q, int):
        return p == q
    elif isinstance(p, TreeNode) and isinstance(q, TreeNode):
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    return False



assert is_same_tree(p=TreeNode(1, 2, 3), q=TreeNode(1, 2, 3)) == True, 'Test 1 Failed'
assert is_same_tree(p=TreeNode(1, 2), q=TreeNode(1, None, 2)) == False, 'Test 2 Failed'
assert is_same_tree(p=TreeNode(1, 2, 1), q=TreeNode(1, 1, 2)) == False, 'Test 3 Failed'