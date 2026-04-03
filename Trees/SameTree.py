class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are null. We reached the end successfully.
        if not p and not q:
            return True
            
        # Base Case 2: One is null, the other isn't. Structure mismatch.
        if not p or not q:
            return False
            
        # Base Case 3: Both nodes exist, but their values don't match.
        if p.val != q.val:
            return False
            
        # Recursive Step: Both current nodes are fine. Now check the children.
        # BOTH the left branches and the right branches must be identical.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)