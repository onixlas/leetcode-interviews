# Same Tree

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**  
Input: `p = [1,2,3], q = [1,2,3]`
Output: `true`

**Example 2:**  
Input: `p = [1,2], q = [1,null,2]`
Output: `false`

**Example 3:**  
Input: `p = [1,2,1], q = [1,1,2]`
Output: `false`

## Solution

```python
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
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

### Explanation of the Solution

This algorithm checks if two binary trees are identical by performing a depth-first comparison:

1. Base Cases:
    * If both nodes are `None` (reached leaf nodes), return `True`
    * If both nodes are integers, compare their values
    * If one is `None` and the other isn't, trees aren't identical (returns `False`)
2. Tree Comparison:
    * First compares current node values
    * Then recursively compares left subtrees and right subtrees
    * Only returns `True` if all corresponding nodes match in both structure and value
3. Termination:
    * If any comparison fails at any level, immediately returns `False`
    * Only returns `True` if entire trees are traversed successfully with all nodes matching

The algorithm effectively performs a simultaneous traversal of both trees, comparing nodes at each step. The worst-case scenario occurs when the trees are identical, requiring a full traversal of all nodes.