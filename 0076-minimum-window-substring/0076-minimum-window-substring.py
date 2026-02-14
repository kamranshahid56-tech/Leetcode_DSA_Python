class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        # Dictionary to keep track of all the unique characters in t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Number of unique characters in t that need to be present in the window
        required = len(dict_t)
        
        # Current window character counts
        window_counts = {}
        
        # 'formed' tracks how many unique characters meet the required frequency
        formed = 0
        
        # (window length, left, right)
        ans = float("inf"), None, None
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character's frequency matches its frequency in t
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]

                # Update the smallest window found so far
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at 'l' is no longer part of the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1    

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]