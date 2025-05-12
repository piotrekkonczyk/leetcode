class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        curr_str = ""
        for i in range(len(s1)):
            curr_str += s2[i]

        right = len(curr_str)
        left = 0

        s1 = str(sorted(s1))

        while right < len(s2):
            if str(sorted(curr_str)) == s1:
                return True
            else:
                right += 1
                left += 1
                curr_str = s2[left:right]

        return str(sorted(curr_str)) == s1


solution = Solution()
print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
print(solution.checkInclusion(s1="ab", s2="eidboaoo"))
print(solution.checkInclusion(s1="adc", s2="dcda"))
