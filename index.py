class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ans = True
        len = 0
        dct = []
        if x < 0:
        	return False
        while x > 0:
        	dct.append(x % 10)
        	x /= 10
        	len += 1
        #print("%d\n" % (len/2))
        for i in range(0, len/2):
        	if len % 2:
	        	if not (dct[len/2 - i - 1] == dct[len/2 + i + 1] and ans):
	        		ans = False
	        		break
	        else:
	        	if not (dct[len/2 -1 - i] == dct[len/2 + i] and ans):
	        		ans = False
	        		break
        return ans

my_test = Solution()
sample = [121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021]

for m in sample:
  print("%d => %r" % (m, my_test.isPalindrome(m)))
