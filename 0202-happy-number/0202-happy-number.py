class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                # Get the last digit using modulo, square it, and add to sum
                digit = number % 10
                total_sum += digit ** 2
                # Remove the last digit using integer division
                number //= 10
            return total_sum

        slow = n
        fast = get_next(n)
        
        # Move pointers until they meet or fast hits 1
        while fast != 1 and slow != fast:
            slow = get_next(slow)          # One step
            fast = get_next(get_next(fast)) # Two steps
            
        return fast == 1
        