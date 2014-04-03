Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import os
>>> import Palindrome
>>> import doctest
>>> 
>>> doctest.testmod(Palindrome, verbose=True)
Trying:
    type(isPalindrome("bob"))
Expecting:
    <type 'bool'>
ok
Trying:
    isPalindrome("abc")
Expecting:
    False
ok
Trying:
    isPalindrome("bob")
Expecting:
    True
ok
Trying:
    isPalindrome("a man a plan a canal, panama")
Expecting:
    True
ok
Trying:
    isPalindrome("A man a plan a canal, Panama")
Expecting:
    False
ok
Trying:
    isPalindrome("A man a plan a canal, Panama", ignorecase=True)
Expecting:
    True
ok
1 items had no tests:
    Palindrome
1 items passed all tests:
   6 tests in Palindrome.isPalindrome
6 tests in 2 items.
6 passed and 0 failed.
Test passed.
TestResults(failed=0, attempted=6)
>>> 