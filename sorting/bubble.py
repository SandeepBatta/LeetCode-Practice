# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

# Time complexity: O(N²)
# Space complexity: O(1)


def bubble(array: list[int]) -> None:
    # Traverse through all array elements
    for idx1 in range(len(array)):
        # Last idx1 elements are already sorted
        for idx2 in range(len(array) - idx1 - 1):
            if array[idx2] > array[idx2 + 1]:
                array[idx2], array[idx2 + 1] = array[idx2 + 1], array[idx2]
