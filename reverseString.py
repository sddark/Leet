class Solution:
    def reverseString(self, s: List[str]) -> None:
        range2 = math.floor(len(s)/2)
        for x in range(0, range2):
            s[x], s[len(s) -x -1] = s[len(s) -x -1], s[x]