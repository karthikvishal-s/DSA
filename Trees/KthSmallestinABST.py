class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use class variables to avoid scope issues
        self.n = 0
        self.result = None

        def travel(node):
            # Base case: if node is null OR we already found the result, stop exploring!
            if not node or self.result is not None:
                return
            
            # 1. Go Left
            travel(node.left)
            
            # 2. Process Current Node
            self.n += 1 
            if self.n == k:
                self.result = node.val
                return # Early exit for this branch
            
            # 3. Go Right
            travel(node.right)

        travel(root)
        return self.result