<?php

class Solution {

  /**
   * @param Integer $x
   * @return Boolean
   */
  function isPalindrome($x) {
  	if($x < 0 || ($x % 10 == 0 && $x != 0)) return false;
  	$revertNum = 0;
  	while($x > $revertNum) {
  		if($revertNum > 0) $revertNum *= 10;
  		$revertNum += $x % 10;
  		$x = (int)($x/10);
  	}
  	return $x == $revertNum || (int)($revertNum / 10) == $x;
  }
}

$sample = array(121, -121, 10, 1221, 3, 12345, 4132314, 100, 4000, 1000021, 0);
$testSolution = new Solution();
foreach ($sample as &$m) {
	echo $m.' => '.($testSolution->isPalindrome($m) ? 'true' : 'false')."\n";
}
?>