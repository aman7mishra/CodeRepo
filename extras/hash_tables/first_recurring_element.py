"""
Return the first recurring element in an array

Input - [1,24,6,7,1,6]
Output - 1
"""

def check_rep(arr):
    """
    Returns the first repeated element
    """
    hash_set = set()
    for element in arr:
        if hash_set.intersection({element}) == {element}:
            print(element)
            break
        else:
            hash_set.add(element)

check_rep([2,2,1,24,6,7,1,6])

