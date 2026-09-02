class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []  # Pairs: (start_index, height)
        
        for i, h in enumerate(heights):
            start = i
            # Look at the height of the last item in the stack: stack[-1][1]
            while stack and stack[-1][1] > h:
                pop_idx, pop_h = stack.pop()
                max_area = max(max_area, pop_h * (i - pop_idx))
                start = pop_idx
            
            stack.append((start, h))
            
        # Process elements left over in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area

