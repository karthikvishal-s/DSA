class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function that takes the current node AND the max value seen on its path
        def dfs(node, max_so_far) -> int:
            if not node:
                return 0
                
            res = 0
            # 1. Is this current node "good"? If yes, add 1 to res.
            # (Your logic goes here)
            if max_so_far<=node.val:
                res+=1

            # 2. What is the new max_so_far that we need to pass to the children?
            # (Your logic goes here)
            new_max=max(max_so_far,node.val)
            
            # 3. Recursively call DFS on the left and right children, adding their results to res
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            
            return res

        # Kick off the DFS using the root node. 
        # The maximum value seen so far at the very beginning is just the root's value!
        return dfs(root, root.val)