class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_set = {}
        chars_set = {}
        for char,chars in zip(t,s):
            if char in char_set:
                char_set[char]+=1
            else:
                char_set[char] = 1

            if chars in chars_set:
                chars_set[chars]+=1
            else:
                chars_set[chars] = 1
        if char_set == chars_set:
            return True
        else:
            return False
        