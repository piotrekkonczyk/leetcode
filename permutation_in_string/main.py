class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for char in s1:
            s1_counts[ord(char) - 97] += 1  # 97 is lowercase "a"

        for right in range(len(s2)):
            width = right - left + 1

            if width < len(s1):
                s2_counts[ord(s2[right]) - 97] += 1
                continue

            if left > 0:
                s2_counts[ord(s2[left - 1]) - 97] -= 1

            s2_counts[ord(s2[right]) - 97] += 1

            if s1_counts == s2_counts:
                return True

            left += 1

        return False


solution = Solution()
print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
print(solution.checkInclusion(s1="hello", s2="ooolleoooleh"))
print(solution.checkInclusion(s1="abc", s2="cccccbabbbaaaa"))
