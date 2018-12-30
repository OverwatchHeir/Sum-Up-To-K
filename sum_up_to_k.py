
# Given an integer array and a integer k , output all pairs that sum up to k

def sum_up_to_k(array, k):

    # Approach:
        # We work with an array without duplicates
        # We ask if tje complement is in the original array
            # If true, we remove it

    array_set = set(array)
    array = list(array_set)

    for element in array:

        complement = k - element
        array_set.remove(element)

        if complement in array_set:
            print(element, complement)





array = [1, 3 , 2, 3, 2, 5, 46, 6, 7, 4, 0]
k = 5

sum_up_to_k(array, k)