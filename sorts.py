def bubble_sort(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            yield [i,None]
            yield [i+1,None]
            if our_list[i] > our_list[i+1]:
                # Swap
                yield [i+1,i]
                yield [i,i+1]
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True

        num_of_iterations += 1


def insertion_sort(our_list):

        for step in range(1, len(our_list)):
            key = our_list[step]
            yield [step,None]
            j = step - 1

            while j >= 0 and key < our_list[j]:
                yield [j,None]
                yield [j, j + 1]
                our_list[j + 1] = our_list[j]

                j = j - 1


            our_list[j + 1] = key
            yield [None, j + 1]


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    yield [i,None]
    yield [l,None]
    if l < n and arr[i] < arr[l]:
        largest = l

    yield [largest,None]
    yield [r,None]
    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield [largest,i]
        yield [i,largest]
        yield from heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        yield from heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        yield [0,i]
        yield [i,0]

        # Heapify root element
        yield from heapify(arr, i, 0)



def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    yield [high,None]

    for j in range(low, high):

        # If current element is smaller
        # than or equal to pivot
        yield [j,None]
        if arr[j] <= pivot:
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield [j,i]
            yield [i,j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield [high,i+1]
    yield [i+1,high]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = yield from partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        yield from quickSort(arr, low, pi - 1)

        yield from quickSort(arr, pi + 1, high)


def merge_inplace(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        yield [mid,None]
        yield [start2,None]
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            yield [start,None]
            yield [start2,None]
            start += 1
        else:
            value = arr[start2]
            yield [start2,None]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                yield [index - 1,index]
                index -= 1

            arr[start] = value
            yield [None,start]

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


'''
* l is for left index and r is right index of
the sub-array of arr to be sorted
'''


def mergeSort_inplace(arr, l, r):
    if (l < r):
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        yield from mergeSort_inplace(arr, l, m)
        yield from mergeSort_inplace(arr, m + 1, r)

        yield from merge_inplace(arr, l, m, r)


def cycleSort(array):
    writes = 0

    # Loop through the array to find cycles to rotate.
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]
        yield [cycleStart,None]

        # Find where to put the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            yield [i,None]
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            yield [pos,None]
            pos += 1
        array[pos], item = item, array[pos]
        yield [None,pos]
        yield [pos,None]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                yield [i,None]
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                yield [pos,None]
                pos += 1
            array[pos], item = item, array[pos]
            yield [None,pos]
            yield [pos,None]
            writes += 1

    return writes


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            yield [i,None]
            yield [i+1,None]
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                yield [i+1,i]
                yield [i,i+1]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            yield [i,None]
            yield [i+1,None]
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                yield [i+1,i]
                yield [i,i+1]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1


def shellSort(arr, n):
    # code here
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                yield [i + gap, None]
                yield [i, None]
                if arr[i + gap] > arr[i]:

                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    yield [i, i + gap]
                    yield [i + gap, i]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2

