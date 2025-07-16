class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 1

                while num + curr in nums_set:
                    curr += 1

                longest = max(longest, curr)

        return longest


solution = Solution()
print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(solution.longestConsecutive(nums=[1, 0, 1, 2]))
print(solution.longestConsecutive(nums=[0, -1]))
