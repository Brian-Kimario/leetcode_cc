class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}  
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i  
            
        return False
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # value -> most recent index
        for i, num in enumerate(nums):
        # Check if duplicate exists within window of size k
            if num in seen and i - seen[num] <= k:
            return True
         # Always update to the most recent index
            seen[num]
        return False
'''