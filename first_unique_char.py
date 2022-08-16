from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, character in enumerate(s):
            if c[character] == 1:
                return i
        return -1

def runTest(input: str, output: int):
    s = Solution()
    assert output == s.firstUniqChar(input)

runTest('leetcode', 0)
runTest('loveleetcode', 2)
runTest('aabb', -1)
