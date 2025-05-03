class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        pair = [0, 0]

        primary_length = len(nums)

        for i in range(primary_length):
            if nums[i] != pair[0]:
                pair[0] = nums[i]
                pair[1] = 0

            if pair[1] < 2:
                nums.append(nums[i])
                pair[1] += 1
                k += 1

        idx = 0

        for i in range(primary_length, len(nums)):
            nums[idx] = nums[i]
            idx += 1

        return k


solution = Solution()
print(solution.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
