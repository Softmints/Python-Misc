def isPalindrome(s, ignorecase=False):

    """
    >>> type(isPalindrome("bob"))
    <type 'bool'>
    >>> isPalindrome("abc")
    False
    >>> isPalindrome("bob")
    True
    >>> isPalindrome("a man a plan a canal, panama")
    True
    >>> isPalindrome("A man a plan a canal, Panama")
    False
    >>> isPalindrome("A man a plan a canal, Panama", ignorecase=True)
    True
    """

    onlyletters = []

    x = 0

    if ignorecase == True:
        s = str.lower(s)

    while x < len(s):
        if str.isalpha(s[x]):
            onlyletters.append (s[x])
        x = x + 1

    reverse = onlyletters[::-1]

    if onlyletters == reverse:
        return True
    else:
        return False



    # Create an empty string "onlyLetters"
    # Loop over all characters in the string argument, and add each 
    #   character which is a letter to "onlyletters"

    # Reverse "onlyletters" and test if this is equal to "onlyletters"
