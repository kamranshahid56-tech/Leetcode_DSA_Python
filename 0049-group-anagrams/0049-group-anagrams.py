class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        Str = []
        for s in strs:
            s1 = tuple(sorted(s))
            if s1 not in freq_map:
                freq_map[s1] = []

            freq_map[s1].append(s)

        return list(freq_map.values())

        

        