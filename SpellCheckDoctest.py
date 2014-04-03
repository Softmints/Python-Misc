Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import SpellCheckFinal
>>> import doctest
>>> doctest.testmod(SpellCheckFinal, verbose = True)
Trying:
    spellCheck("test1.txt")
Expecting:
    {'exercsie': 1, 'finised': 1}
ok
Trying:
    spellCheck("test2.txt")
Expecting:
    {'bechause': 1, 'c++': 1}
ok
Trying:
    spellCheck("test3.txt")
Expecting:
    {'lissard': 1, 'chamelon': 1, 'gerbal': 2, 'hampster': 3, 'tortise': 1}
ok
Trying:
    type(spellCheck("test1.txt"))
Expecting:
    <type 'dict'>
ok
1 items had no tests:
    SpellCheckFinal
1 items passed all tests:
   4 tests in SpellCheckFinal.spellCheck
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
TestResults(failed=0, attempted=4)
>>> 