class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_set = {}
        chars_set = {}
        for char,chars in zip(t,s):

            char_set[char] = char_set.get(char,0)+1
            
            chars_set[chars] = chars_set.get(chars,0)+1

        return char_set == chars_set
        