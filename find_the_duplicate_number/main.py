class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                return nums[i]

        return nums[-1]


solution = Solution()
print(solution.findDuplicate(nums=[1, 3, 4, 2, 2]))
print(solution.findDuplicate(nums=[3, 1, 3, 4, 2]))
