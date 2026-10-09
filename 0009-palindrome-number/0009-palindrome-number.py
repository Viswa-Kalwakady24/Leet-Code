class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        n=x
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if rev==n:
            return True
        else:
            return False

        