# The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted.

# Time complexity: O(N²)
# Space complexity: O(1)


def selection(array: list[int]) -> None:
    # Traverse through all array elements
    for idx1 in range(len(array)):
        sub_array_min_idx = idx1
        # Find the minimum element in remaining unsorted portion of array
        for idx2 in range(idx1 + 1, len(array)):
            if array[idx2] < array[idx1]:
                sub_array_min_idx = idx2
        array[idx1], array[sub_array_min_idx] = array[sub_array_min_idx], array[idx1]
