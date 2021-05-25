#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.



class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(x)[::-1]) if x>=0 else -int(str(abs(x))[::-1])

        return rev if abs(rev)<=2**31-1 else 0
