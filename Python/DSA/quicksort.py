def quicksort(array):
    """
    Implements the Quicksort algorithm to sort an array.

    Parameters:
    array (list): The list of numbers to be sorted.

    Returns:
    list: A new sorted list in ascending order.
    """

    # Base Case: If the array has 0 or 1 element, it is already sorted.
    if len(array) < 2:
        return array  

    # Recursive Case:
    pivot = array[0]  # Choose the first element as the pivot

    # List comprehension to partition the array
    less = [i for i in array[1:] if i <= pivot]  # Elements less than or equal to pivot
    greater = [i for i in array[1:] if i > pivot]  # Elements greater than pivot

    # Recursively sort the sublists and combine the results
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    # Example usage
    test_list = [10, 5, 2, 3]
    sorted_list = quicksort(test_list)
    print(sorted_list)  # Output: [2, 3, 5, 10]
