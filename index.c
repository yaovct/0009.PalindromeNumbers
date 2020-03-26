#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool isPalindrome(int x){
	if(x < 0 || (x % 10 == 0 && x != 0)) return false;
	int revertNum = 0;
	while(x > revertNum) {
		if(revertNum > 0) revertNum *= 10;
		revertNum += x % 10;
		x /= 10;
	}
	return x == revertNum || revertNum/10 == x;
}

int main(int argc, char *argv[]) {

  int sample[] = {121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021, 0};
  for(int i=0; i<sizeof(sample)/sizeof(sample[0]); i++) {
		printf("%d => %d\n", sample[i], isPalindrome(sample[i]));
	}
}