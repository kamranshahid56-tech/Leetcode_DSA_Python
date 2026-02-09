class Solution:
    def isPalindrome(self, s: str) -> bool:
        lr = s.lower()
        new = re.sub(r'[^a-z0-9]','',lr)   
        n = len(new)
        l,r = 0,n-1
        while l < r:
            if new[l] != new[r]:
                return False
            l+=1
            r-=1
        return True