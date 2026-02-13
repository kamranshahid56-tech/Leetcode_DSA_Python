class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        window_counts = {}
        l = 0
        n1,n2 = len(s1),len(s2)
        if n1>n2:
            return False
        for char in s1:
            s1_counts[char] = s1_counts.get(char,0)+1
        
        for r in range(n2):
            window_counts[s2[r]] = window_counts.get(s2[r],0)+1
            
            if (r-l+1)>n1:
                window_counts[s2[l]]-=1
                if window_counts[s2[l]] == 0:
                    del window_counts[s2[l]]
                l+=1
            if window_counts == s1_counts:
                return True
        return False
