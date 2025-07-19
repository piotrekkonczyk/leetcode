class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {"b", "a", "l", "o", "n"}
        counts = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        balloons = 0

        for char in text:
            if char not in letters:
                continue

            counts[char] += 1

        while counts:
            for k in counts:
                counts[k] -= 1

                if counts[k] == -1:
                    return balloons

            counts["l"] -= 1
            counts["o"] -= 1

            if counts["l"] == -1 or counts["o"] == -1:
                return balloons

            balloons += 1

        return balloons


solution = Solution()
print(solution.maxNumberOfBalloons(text="nlaebolko"))
print(solution.maxNumberOfBalloons(text="loonbalxballpoon"))
print(solution.maxNumberOfBalloons(text="leetcode"))
