Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> import doctest
>>> import Doomsday
>>> 
>>> doctest.testmod(Doomsday, verbose=True)
Trying:
    doomsday(2012)
Expecting:
    3
ok
Trying:
    doomsday(1899)
Expecting:
    2
ok
Trying:
    doomsday(1923)
Expecting:
    3
ok
Trying:
    doomsday(10000)
Expecting:
    -1
ok
Trying:
    doomsday(1756)
Expecting:
    -1
ok
Trying:
    type(doomsday(2010))
Expecting:
    <type 'int'>
ok
1 items had no tests:
    Doomsday
1 items passed all tests:
   6 tests in Doomsday.doomsday
6 tests in 2 items.
6 passed and 0 failed.
Test passed.
TestResults(failed=0, attempted=6)
>>> 