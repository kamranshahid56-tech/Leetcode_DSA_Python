class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[^a-zA-Z0-9]','',s)   
        n = len(new)
        l,r = 0,n-1
        while l < r:
            if new[l].lower() != new[r].lower():
                return False
            l+=1
            r-=1
        return True