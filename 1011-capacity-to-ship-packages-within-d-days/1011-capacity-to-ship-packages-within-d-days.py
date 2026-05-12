class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        
        # Helper function to check if a capacity 'mid' can ship within 'days'
        def canShip(capacity):
            ships = 1
            curr_cap = capacity
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = capacity
                curr_cap -= w
            return ships <= days

        # Binary search for the minimum capacity
        while l <= r:
            mid = l + (r - l) // 2
            if canShip(mid):
                res = mid
                r = mid - 1 # Try to find a smaller capacity
            else:
                l = mid + 1 # Need a bigger capacity
                
        return res