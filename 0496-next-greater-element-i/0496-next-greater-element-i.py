class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                popped_element = stack.pop()
                nge_map[popped_element] = num

            stack.append(num)

        return [nge_map.get(num,-1) for num in nums1]        