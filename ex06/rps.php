<?php
echo "Choose rock, paper, or scissors: ";
$str = rtrim(fgets(STDIN));
$arr = array("rock", "paper", "scissors");
$idx = array_search($str, $arr);
if ($idx === false) {
    echo "Wrong input\n";
    return ;
}
$tmp = array_rand($arr);
$res = $arr[$tmp];
if ($tmp == $idx) {
	echo "Drew. The computer chose $res.\n";
}
elseif ($tmp == ($idx + 1) % 3) {
    echo "Sorry, you lost. The computer chose $res.\n";
}
else {
	echo "Congratulations! You won! The computer chose $res.\n";
}
?>
