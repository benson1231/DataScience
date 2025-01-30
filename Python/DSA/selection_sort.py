def find_smallest(arr):
    """
    Finds the index of the smallest element in the list.

    Parameters:
    arr (list): A list of numbers.

    Returns:
    int: The index of the smallest element in the list.
    """

    smallest = arr[0]  # Assume the first element is the smallest
    smallest_index = 0  # Store the index of the smallest element

    # Iterate through the list starting from index 1
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]  # Update the smallest value
            smallest_index = i  # Update the index of the smallest value

    return smallest_index  # Return the index of the smallest element


def selection_sort(arr):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: A new sorted list.
    """

    new_arr = []  # Create a new list to store sorted elements

    for _ in range(len(arr)):  # Loop until all elements are moved to new_arr
        smallest_index = find_smallest(arr)  # Find the index of the smallest element
        new_arr.append(arr.pop(smallest_index))  # Remove the smallest element and append to new_arr

    return new_arr  # Return the sorted list


if __name__ == "__main__":
    # Example usage: Only runs when this file is executed directly
    test_list = [5, 3, 6, 2, 10]
    sorted_list = selection_sort(test_list)
    print(sorted_list)  # Output: [2, 3, 5, 6, 10]
