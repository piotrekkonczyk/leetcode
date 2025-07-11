class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        letters = [0] * 26

        for right in range(len(s)):
            letters[ord(s[right]) - 65] += 1  # 65 is for 'A'

            while right - left + 1 - max(letters) > k:
                letters[ord(s[left]) - 65] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
print(solution.characterReplacement(s="ABAB", k=2))
print(solution.characterReplacement(s="AABABBA", k=1))
print(solution.characterReplacement(s="ABBB", k=2))
