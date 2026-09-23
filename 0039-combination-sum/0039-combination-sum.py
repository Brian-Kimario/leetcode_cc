class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(index, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))
                return
            
            for i in range(index, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()
                
        backtrack(0, [], 0)
        return result
