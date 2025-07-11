class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        longest = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

                while zeros > k:
                    if nums[left] == 0:
                        zeros -= 1

                    left += 1

            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
print(solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(
    solution.longestOnes(
        nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
    )
)
