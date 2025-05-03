class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix[0])
        m = len(matrix)

        top, right, bottom, left = 0, n, m, 0
        curr_direction = "right"

        col = 0
        row = 0

        nums: list[int] = []

        for _ in range(m * n):
            if curr_direction == "right" and col + 1 == right:
                top += 1
                curr_direction = "bottom"
            elif curr_direction == "bottom" and row + 1 == bottom:
                right -= 1
                curr_direction = "left"
            elif curr_direction == "left" and col == left:
                bottom -= 1
                curr_direction = "top"
            elif curr_direction == "top" and row == top:
                left += 1
                curr_direction = "right"

            nums.append(matrix[row][col])

            if curr_direction == "right":
                col += 1
            elif curr_direction == "bottom":
                row += 1
            elif curr_direction == "left":
                col -= 1
            else:
                row -= 1

        return nums


solution = Solution()
print(solution.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.spiralOrder(matrix=[[3], [2]]))
