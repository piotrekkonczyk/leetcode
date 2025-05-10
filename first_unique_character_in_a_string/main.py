class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap: dict[str, int] = {}

        N = len(s)

        for i in range(N):
            if s[i] in hashmap:
                hashmap[s[i]] = N
            else:
                hashmap[s[i]] = i

        min_idx = min(hashmap.values())

        if min_idx == N:
            return -1

        return min_idx


solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
print(solution.firstUniqChar("aadadaad"))
