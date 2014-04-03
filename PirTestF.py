def survivor(names, step):
	"""
    >>> survivor([1,2,3,4,5,6,7,8],3)
    7
    >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3)
    'Greg'
    >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 1)
    'Harriet'
    >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 6)
    'Andrew'
    >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 2)
    'Andrew'
    >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 4)
    'Felicity'
    >>> type(survivor([1,2,3,4,5,6,7,8],3))
    <type 'int'>
    >>> type(survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3))
    <type 'str'>
    >>> safeN(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], "Greg")
    3
    >>> safeN(range(1,11), 5)
    2
    >>> safeN(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], "Harriet")
    1
    >>> safeN(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], "Andrew")
    2
    >>> type(safeN(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], "Craig"))
    <type 'int'>
    """

	x = step - 1
	next = step - 1

	while len(names) > 1:
		names.pop(next)
		next = (next + x) % len(names)
	return names[0]


def safeN(names, name):

    new = names[:]
    count = 1
    Loop = survivor(new, count) == name

    while Loop == False:
        new = names[:]
        count = count + 1
        Loop = survivor(new, count) == name
    return count