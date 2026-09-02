class Solution(object):
    def subsets(self, nums):
        result = []
        
        def backtrack(start_idx, current_subset):
            # Every step along the decision tree is a valid subset
            result.append(list(current_subset))
            
            # Explore decisions for remaining elements
            for i in range(start_idx, len(nums)):
                # 1. Choose the current element
                current_subset.append(nums[i])
                
                # 2. Recurse to consider subsequent elements
                backtrack(i + 1, current_subset)
                
                # 3. Undo choice (backtrack) to explore alternative combinations
                current_subset.pop()

        backtrack(0, [])
        return result
