from collections import Counter

def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    # First: create dictionary keys -> numbers from 1 to 9.
    # values -> letters substring.
    # keypad = {'0': '', '1': None, '2': 'abc', ..., '9': 'wxyz'}
    # Second: counter numbers. May use module Counter from collections?
    # Third: search in the dict values letters and get correct letter
    # according to the index. The index is calculate as follow:
    # count = Counter(keys)
    # Counter({'4': 2, '3': 2, '5': 6, '6': 3})
    # index = count['4'] - 1

    key_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    value_list = [' ', None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    keypad = dict(zip(key_list, value_list))
    count = Counter(keys)
    breakpoint()
    letter_list = []
    for k, v in count.items():
        if k == '1':
            continue
        if v % 3 == 0:
            _repet = v // 3
        if v % 4 == 0:
            _repet = v // 4
        letter_list.append(keypad[k][index])

    return ''.join(letter_list)

