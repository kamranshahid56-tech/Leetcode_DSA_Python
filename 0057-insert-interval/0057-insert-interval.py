class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        #intervals that come before newInterval
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        # 2. Merge overlapping intervals with the new interval
        # Overlap happens if the current interval starts before the new interval ends
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        # Add the (potentially merged) new interval
        res.append(newInterval)
        # 3. Add the rest of the intervals that come strictly AFTER
        if i < n:
            res.extend(intervals[i:])
        return res


