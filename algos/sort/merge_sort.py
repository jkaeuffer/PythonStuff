# Implementation of Merge Sort Algorithm, using recursion


def merge(left, right):
    result = list()

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)

        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left

    if right:
        result += right

    return result


def merge_sort(array):
    # Base Case: Array is empty, or with 1 element
    if len(array) <= 1:
        return array

    middle_idx = len(array) / 2
    left_arr = array[:middle_idx]
    right_arr = array[middle_idx:]

    lefty = merge_sort(left_arr)
    righty = merge_sort(right_arr)

    return merge(lefty, righty)


lst1 = [0, 2, 4, 1, -5, 45]

print "Unsorted: "
print lst1

lst1_sorted = merge_sort(lst1)

print "Sorted: "
print lst1_sorted

print "Original List: "
print lst1
