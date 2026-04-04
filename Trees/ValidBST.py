class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to pass the boundaries down the tree
        def validate(node, left_bound, right_bound):
            # Base case: An empty node is valid
            if not node:
                return True
            
            # 1. CHECK YOURSELF: Does the current node break the rules?
            # It must be strictly greater than the left bound, and strictly less than the right bound.
            if not (left_bound < node.val < right_bound):
                return False
            
            # 2. CHECK CHILDREN: Pass the updated bounds down.
            # When going left, the current node's value becomes the new strict MAXIMUM.
            valid_left = validate(node.left, left_bound, node.val)
            
            # When going right, the current node's value becomes the new strict MINIMUM.
            valid_right = validate(node.right, node.val, right_bound)
            
            # Both sides must be true!
            return valid_left and valid_right

        # Kick off the recursion with infinite boundaries
        return validate(root, float('-inf'), float('inf'))