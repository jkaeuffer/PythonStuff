# Implementation of the Quick Sort Algorithm
# Worst Case Running Time O(N * logN)

from random import randrange, shuffle 
def quicksort(list1, start, end):
  # this portion of list has been sorted
  if start >= end:
    return

  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list1[pivot_idx]

  # swap random element with last element in sub-list1ay
  list1[end], list1[pivot_idx] = list1[pivot_idx], list1[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list1[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list1[i], list1[less_than_pointer] = list1[less_than_pointer], list1[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list1[end], list1[less_than_pointer] = list1[less_than_pointer], list1[end]
  
  # Call quicksort on the "left" and "right" sub-list1s
  quicksort(list1, start, less_than_pointer - 1)
  quicksort(list1, less_than_pointer + 1, end)
  
  
unsorted_list1 = [3,7,12,24,36,42]
shuffle(unsorted_list1)
print(unsorted_list1)
# use quicksort to sort the list1, then print it out!

quicksort(unsorted_list1, 0, len(unsorted_list1) - 1)
print(unsorted_list1)