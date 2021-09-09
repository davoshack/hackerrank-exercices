class A:
    def f(self):
        '''
        Function descripton, argument types,
        return type ...
        >>> a = A()
        >>> a.f()
        Hello world
        'Hello world'
        '''
        print ('Hello world')
        return 'Hello world'

    @property
    def error(self):
        '''
        This function just errors
        >>> A().error
        Traceback (most recent call last):
        ...
        Exception: I am an error
        '''
        raise Exception("I am an error")

def f(x):
    '''
    >>> f(10)
    Args: 10
    'Valid input'
    >>> f(-1)
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    '''
    if x <= 0:
        raise ValueError('Invalid input')
    print(f"Args: {x}")
    return "Valid input"


def g(x):
    # assert <condition>, [<error>]
    assert x > 0, "Invalid input"


def lst_one_more(lst1, lst2):
    '''
    This will mutate lst1 so that at index
    `i`, lst1[i] = lst2[i] + 1
    lst1 and lst2 should be the same length
    '''
    assert len(lst1) == len(lst2), "length of lists not the same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1

lst1 = [1, 1, 1, 1]
lst2 = [1, 2, 3]
lst_one_more(lst1, lst2)
for i, x in enumerate(lst1):
    assert x == lst2[i] + 1
    # print(x, lst2[i])

