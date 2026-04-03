class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper Function: Handles VERIFICATION
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


        # --- Main Function: Handles TRAVERSAL ---
        
        # 1. Base Case: If the main tree is empty, it can't have a subtree
        if not root:
            return False
            
        # 2. Check the current node: Are they identical right here?
        if isSameTree(root, subRoot):
            return True
            
        # 3. Recursive Traversal: If not identical here, dig deeper into the main tree.
        # Notice we are calling self.isSubtree to keep moving down the tree!
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)