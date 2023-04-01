print "Enter a string: ";
chomp($tmp = <>);
if ( $tmp eq reverse($tmp)) {
  print "The string is a palindrome!\n";
}
else {
  print "The string is not a palindrome.\n";
}
