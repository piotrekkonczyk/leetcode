class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_characters: set[str] = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen_characters:
                seen_characters.remove(s[left])
                left += 1

            seen_characters.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
print(solution.lengthOfLongestSubstring(s="abcabcbb"))
print(solution.lengthOfLongestSubstring(s="bbbbb"))
