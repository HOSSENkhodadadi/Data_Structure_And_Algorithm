
class Solution:
    def check_is_palindrom(self, s: str) -> bool:
        len_str = len(s)
        if len_str % 2 == 0:
            second_half = s[len(s)//2:]
            second_half = second_half[::-1]
            if second_half == s[:len(s)//2]:
                return True
            else:
                return False
        else:
            second_half = s[len(s)//2 + 1:]
            second_half = second_half[::-1]
            if second_half == s[:len(s)//2]:
                return True
            else:
                return False
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        longest_sub = ""
        for l in range(2, len(s) + 1):
            for i in range(0, len(s)-l+1):
                if self.check_is_palindrom(s[i:i+l]):

                    longest_sub = s[i:i+l]
        return longest_sub

s = "aba"
sol = Solution()
print(sol.longestPalindrome(s))
