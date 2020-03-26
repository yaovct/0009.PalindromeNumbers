/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
	if(x < 0 || (x % 10 == 0 && x!=0)) return false;
	var revertNum = 0;
	while (x > revertNum) {
		if(revertNum > 0) {
			revertNum *= 10;
		}
		revertNum += x % 10;
		x = parseInt(x/10);
	}
	return x == revertNum || parseInt(revertNum/10) == x;
};

var sample = [121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021, 0];
sample.forEach(function (m) {
	console.log(m, isPalindrome(m));
});
