<?php
echo "Choose rock, paper, or scissors: ";
$str = rtrim(fgets(STDIN));
if ($str != "rock" && $str != "paper" && $str != "scissors") {
    echo "Wrong input";
    return ;
}
$tmp = rand(0, 2);
if ($tmp == 0) {
    $res = "rock";
} elseif ($tmp == 1) {
    $res = "paper";
} else {
    $res = "scissors";
}
if ($str == $res) {
    echo "Congratulations! You won! The computer chose $res.";
} else {
    echo "Sorry, you lost. The computer chose $res.";
}
?>
