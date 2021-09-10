from math import floor

def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority elemnt.
    Majority element is the element that appears more than 
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # find majority element
    # if there is no majority element, return []
    # find the indexes of the majority element,
    # put them in a list
    from collections import Counter
    if lst == []:
        return []

    count = Counter(lst)
#    top_elems = sorted(
#        count.keys(),
#        key=lambda x: -count[x]
#    ) # O(nlogn)

    top_count = max(count.values()) # O(n)
    maj_elem = [elem for elem, count 
                in count.items() if count == top_count
    ][0] # O(n)

    # maj_elem = top_elems[0]
    # there exists a majority element
    if count[maj_elem] > len(lst) // 2:
        return [
            i for i, elem in enumerate(lst)
            if elem == maj_elem
        ] # O(n)
    else:
        return []


