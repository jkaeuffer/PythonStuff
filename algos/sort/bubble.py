# Bubble Sort Implementation


def bubble_sort(my_list):
    rounds = len(my_list) - 1
    for i in my_list:
        for n in range(rounds):
            if my_list[n] > my_list[n + 1]:
                my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]


lst1 = [0, 2, 4, 1, -5, 45]

print "Unsorted: "
print lst1

bubble_sort(lst1)

print "Sorted: "
print lst1
