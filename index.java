import java.lang.*;
import java.util.*;

class Solution {
  public boolean isPalindrome(int x) {
  	if(x < 0 || (x % 10 == 0 && x != 0)) return false;
  	int revertNum = 0;
  	while(x > revertNum) {
  		if(revertNum > 0) revertNum *= 10;
  		revertNum += x % 10;
  		x /= 10;
  	}
  	return x == revertNum || revertNum/10 == x;
  }
}

public class index {

	public static void main(String[] args) {
		int [] sample = {121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021, 0};

    Solution demo = new Solution();
    for(int m : sample) {
    	System.out.printf("%d => %b\n", m, demo.isPalindrome(m));
    }
	}
}