class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        N = len(nums)
        prefix, postfix = [0] * N, [0] * N

        curr_sum = 0

        for i in range(N):
            prefix[i] = curr_sum
            curr_sum += nums[i]

        curr_sum = 0

        for i in range(N - 1, -1, -1):
            postfix[i] = curr_sum
            curr_sum += nums[i]

        for i in range(N):
            if prefix[i] == postfix[i]:
                return i

        return -1


solution = Solution()
print(solution.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(solution.pivotIndex(nums=[1, 2, 3]))
print(solution.pivotIndex(nums=[2, 1, -1]))
