class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        smallest = 10**10

        for right in range(len(nums)):
            if nums[right] >= target:
                return 1

            current_sum += nums[right]

            while current_sum >= target:
                smallest = min(smallest, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return smallest if smallest != 10**10 else 0


solution = Solution()
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
