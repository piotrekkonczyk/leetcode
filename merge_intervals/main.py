class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged: list[list[int]] = []
        intervals.sort()

        for interval in intervals:
            if not merged:
                merged.append(interval)
                continue

            if merged[-1][0] <= interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged


solution = Solution()
print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge(intervals=[[1, 4], [4, 5]]))
print(solution.merge(intervals=[[1, 4], [0, 4]]))
