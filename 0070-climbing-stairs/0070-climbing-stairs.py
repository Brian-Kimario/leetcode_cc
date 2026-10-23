class Solution(object):
    def climbStairs(self, n):
        # Base cases handled automatically by loop bounds, but good to explicitly state
        if n <= 2:
            return n
            
        # ordinary fibonacci pointers
        # one_step_back represents ways(i-1), two_steps_back represents ways(i-2)
        two_steps_back = 1
        one_step_back = 2
        
        for i in range(3, n + 1):
            current = one_step_back + two_steps_back
            
            # Shift the window forward for the next iteration
            two_steps_back = one_step_back
            one_step_back = current
            
        return one_step_back
