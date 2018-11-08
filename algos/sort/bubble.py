# Bubble Sort Implementation


# Helper function for swaps
def swap(array, idx_1, idx_2):
    temp = array[idx_1]
    array[idx_1] = array[idx_2]
    array[idx_2] = temp


def bubble_sort(my_list):
    rounds = len(my_list) - 1
    for i in my_list:
        for n in range(rounds):
            if my_list[n] > my_list[n + 1]:
                swap(my_list, n, n + 1)


lst1 = [0, 2, 4, 1, -5, 45]

print "Unsorted: "
print lst1

bubble_sort(lst1)

print "Sorted: "
print lst1
