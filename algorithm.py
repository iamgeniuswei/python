
step = 0
def findSmallest(array):
    global step
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        step += 1
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    array.pop(smallest_index)
    return smallest
            

def selection_sort(array):
    global step
    newArray = []
    for i in range(len(array)):
        step += 1
        smallest = findSmallest(array)
        newArray.append(smallest)
    return newArray

# step = 0
unsort_array = [5, 3, 6, 2, 10, 7]
sort_array = selection_sort(unsort_array)
print(sort_array)

print('The total step is: ', step)
