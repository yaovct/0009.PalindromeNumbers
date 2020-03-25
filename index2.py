# solve it without converting the integer to a string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
        	return False
        revertNum = 0
        while(x > revertNum):
        	if revertNum > 0:
        		revertNum *= 10
        	revertNum += x % 10
        	x /= 10
        #print("%d %d\n" % (x, revertNum))
        return x == revertNum or revertNum/10 == x

my_test = Solution()
sample = [121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021, 0]

for m in sample:
  print("%d => %r" % (m, my_test.isPalindrome(m)))
