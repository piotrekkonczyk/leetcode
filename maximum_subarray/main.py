class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -10000000
        current_sum = 0

        for num in nums:
            if current_sum + num > num:
                current_sum = current_sum + num
            else:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

            max_sum = max(current_sum, max_sum)

        return max_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
