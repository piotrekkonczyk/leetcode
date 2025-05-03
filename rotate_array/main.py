class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        rotated: list[int] = []
        N = len(nums)

        if k > N:
            k = k % N

        for i in range(N - k, N):
            rotated.append(nums[i])

        for i in range(0, N - k):
            rotated.append(nums[i])

        for i in range(N):
            nums[i] = rotated[i]

        print(nums)


solution = Solution()
print(solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(solution.rotate(nums=[-1, -100, 3, 99], k=2))
print(solution.rotate(nums=[1, 2], k=5))
