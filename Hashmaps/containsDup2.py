class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Dictionary to store: { number : last_seen_index }
        seen = {}
        
        for i, num in enumerate(nums):
            # If we've seen the number before AND it's within 'k' distance
            if num in seen and abs(i - seen[num]) <= k:
                return True
                
            # Update the dictionary with the most recent index
            seen[num] = i
            
        return False