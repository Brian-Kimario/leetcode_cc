class Solution(object):
    def canCross(self, stones):
        # Create a mapping of stone position -> set of incoming jump distances
        stone_positions = {stone: set() for stone in stones}
        
        # Base case: to get to the first stone, we simulate an incoming jump of 0
        stone_positions[stones[0]].add(0)
        
        for stone in stones:
            for k in stone_positions[stone]:
                # Try all three possible next jump lengths
                for step in (k - 1, k, k + 1):
                    if step > 0:  # The frog can only jump forward
                        next_stone = stone + step
                        # If a stone exists at that landing coordinate, record the jump
                        if next_stone in stone_positions:
                            stone_positions[next_stone].add(step)
                            
        # If the last stone has received any incoming jumps, the cross is successful
        return len(stone_positions[stones[-1]]) > 0
