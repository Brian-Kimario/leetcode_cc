class Solution {
public:
    int climbStairs(int n) {
        // Create a memo array initialized to -1 (meaning "not calculated yet")
        vector<int> memo(n + 1, -1);
        return climb(0, n, memo);
    }

private:
    int climb(int current, int target, vector<int>& memo) {
        // Base cases
        if (current == target) return 1;
        if (current > target) return 0;
        
        // 1. Check if we have already calculated this step
        if (memo[current] != -1) {
            return memo[current];
        }
        
        // 2. Calculate and store the result in the memo array
        memo[current] = climb(current + 1, target, memo) + 
                        climb(current + 2, target, memo);
        
        return memo[current];
    }
};
