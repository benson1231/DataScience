class BinarySearch:
    """
    A class that implements binary search using both iterative and recursive methods.
    """

    def search_iterative(self, arr, item):
        """
        Performs binary search iteratively.

        Parameters:
        arr (list): A sorted list in which to search for the item.
        item (int/float): The target item to find.

        Returns:
        int: The index of the item if found, otherwise None.
        """

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2  # Compute the middle index
            guess = arr[mid]  # Retrieve the middle element

            if guess == item:  # If the middle element is the target, return its index
                return mid
            elif guess > item:  # If the guess is too high, adjust the high boundary
                high = mid - 1
            else:  # If the guess is too low, adjust the low boundary
                low = mid + 1

        return None  # If the item is not found, return None

    def search_recursive(self, arr, low, high, item):
        """
        Performs binary search recursively.

        Parameters:
        arr (list): A sorted list in which to search for the item.
        low (int): The starting index of the search range.
        high (int): The ending index of the search range.
        item (int/float): The target item to find.

        Returns:
        int: The index of the item if found, otherwise None.
        """

        # Base case: If the search range is valid
        if high >= low:
            mid = (high + low) // 2  # Compute the middle index
            guess = arr[mid]  # Retrieve the middle element

            if guess == item:  # If the middle element is the target, return its index
                return mid
            elif guess > item:  # If the guess is too high, search in the left subarray
                return self.search_recursive(arr, low, mid - 1, item)
            else:  # If the guess is too low, search in the right subarray
                return self.search_recursive(arr, mid + 1, high, item)

        return None  # If the item is not found, return None


if __name__ == "__main__":
    # Initialize the BinarySearch class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]  # Sorted list

    # Testing the iterative method
    print(bs.search_iterative(my_list, 3))  # Output: 1
    print(bs.search_iterative(my_list, -1))  # Output: None

    # Testing the recursive method
    print(bs.search_recursive(my_list, 0, len(my_list) - 1, 7))  # Output: 3
    print(bs.search_recursive(my_list, 0, len(my_list) - 1, 10))  # Output: None
