def fizz_buzz(numbers):
    '''
    Given a list of integers:
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    for i, num in enumerate(numbers):
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"
        elif num % 3 == 0:
            numbers[i] = "fizz"
        elif num % 5 == 0:
            numbers[i] = "buzz"

