class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        def travel(node):
            # Base case: if we hit a null node, just bounce back up
            if not node:
                return
            
            # 1. Go all the way LEFT
            travel(node.left)
            
            # 2. Process the CURRENT node
            stack.append(node.val)
            
            # 3. Go all the way RIGHT
            travel(node.right)

        travel(root)
        return stack[k-1]