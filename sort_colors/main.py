class Solution:
    def sortColors(self, nums: list[int]) -> None:
        hashmap = {0: 0, 1: 0, 2: 0}

        for num in nums:
            hashmap[num] += 1

        idx = 0

        for _ in range(hashmap[0]):
            nums[idx] = 0
            idx += 1
        for _ in range(hashmap[1]):
            nums[idx] = 1
            idx += 1
        for _ in range(hashmap[2]):
            nums[idx] = 2
            idx += 1

        print(nums)


solution = Solution()
print(solution.sortColors(nums=[2, 0, 2, 1, 1, 0]))
print(solution.sortColors(nums=[2, 0, 1]))
