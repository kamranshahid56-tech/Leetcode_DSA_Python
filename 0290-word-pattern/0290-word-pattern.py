class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Base case: lengths must match
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        # Use zip to iterate through both simultaneously
        for char, word in zip(pattern, words):
            # Check char -> word mapping
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Check word -> char mapping
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True