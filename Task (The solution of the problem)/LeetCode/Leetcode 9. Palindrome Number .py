class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            g = str(x)
            for item in range(0, len(g) // 2, 1):
                if g[item] == g[-1]:
                    g = g[0:-1]
                else:
                    return False
                    pass
            return True
            pass
        else:
            return False
