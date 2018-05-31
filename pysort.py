from random import shuffle
from time import sleep
from display import *
import threading
x = 0
# bubble Sort

def bubble_sort(a_list, fig):
    for i in range(1, len(a_list)):
        for j in range(1, len(a_list)):
            if a_list[j - 1] > a_list[j]:
                (a_list[j], a_list[j - 1]) = (a_list[j - 1], a_list[j])
                x = display(a_list, fig)
                if x == -1:
                    x = 0
                    return a_list
    return a_list

# Insertion Sort
def insertion_sort(a_list, fig):
    for i in range(1, len(a_list)):
        while i > 0 and a_list[i - 1] > a_list[i]:
            (a_list[i], a_list[i - 1]) = (a_list[i - 1], a_list[i])
            i -= 1
            x = display(a_list, fig)
            if x == -1:
                x = 0
                return a_list
    return a_list

# Selection Sort
def selection_sort(a_list, fig):
    for i in range(len(a_list)):
        min_pos = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_pos]:
                min_pos = j
        (a_list[min_pos], a_list[i]) = (a_list[i], a_list[min_pos])
        x = display(a_list, fig)
        if x == -1:
            x = 0
            return a_list
    return a_list

# Quick Sort
def quick_sort_exec(some_list, start, stop, fig):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                print("Swapping", some_list[left], "with", some_list[right])
                left += 1
                right -= 1

        display(some_list, fig)

        quick_sort_exec(some_list, start, right, fig)
        quick_sort_exec(some_list, left, stop, fig)


def quicksort(a_list, fig):
    low = 0
    high = len(a_list) - 1
    a_list = quick_sort_exec(a_list, low, high, fig)
    return a_list
# counting sort
def counting_sort(a_list, fig):

    # we need three more lists:
    # index, count, output
    temp = a_list.copy()
    # index has a length equal to the maximum element
    index = [i for i in range(max(a_list) + 1)]

    # count has length equal to the index
    count = [0 for i in range(len(index))]

    # now we must count the elements
    for i in range(len(a_list)):
        count[a_list[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i -1]

    for i in range(len(temp)):
        locate = index.index(temp[i])
        print(count)
        count[locate] -= 1
        print(count)
        a_list[count[locate]] = temp[i]
        x = display(a_list, fig)
        if x == -1:
            return a_list
    return a_list

# Merge Sort
def merge_sort(a_list, fig):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]

        merge_sort(lefthalf, fig)
        merge_sort(righthalf, fig)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k] = lefthalf[i]
                i += 1
            else:
                a_list[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i += 1
            k += 1
            display(a_list, fig)
        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j += 1
            k += 1
            display(a_list, fig)
    display(a_list, fig)
    return a_list

# Bogosort
def inorder(a_list):
    i = 0
    j = len(a_list)
    while i + 1 < j:
        if a_list[i] > a_list[i + 1]:
            return False
        i += 1
    return True


def bogosort(a_list, fig):
    while not inorder(a_list):
        shuffle(a_list)
        x = display(a_list, fig)
        if x == -1:
            x = 0
            return a_list
    return a_list

# Comb Sort
def comb_sort(a_list, fig):
    gap = len(a_list)
    swaps = True

    while gap > 1 or swaps:
        gap = len(a_list)
        swaps = True

        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))
            swaps = False

            for i in range(len(a_list) - gap):
                j = i + gap
                if a_list[i] > a_list[j]:
                    (a_list[i], a_list[j]) = (a_list[j], a_list[i])
                    display(a_list, fig)
                    swaps = True
    return a_list

# Bitonic Sort
def isPowerOf2(num):
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def reform(a_list):
    while isPowerOf2(len(a_list)) != True:
        a_list.append(0)
    return a_list


def restore(a_list):
    while 0 in a_list:
        a_list.remove(0)


def compAndSwap(
    a_list,
    i,
    j,
    direction,
    ):

    if direction == 1 and a_list[i] > a_list[j] or direction == 0 \
        and a_list[j] > a_list[i]:
        (a_list[i], a_list[j]) = (a_list[j], a_list[i])


def bitonicMerge(a_list, low, center, direction, fig):

    if center > 1:
        k = center // 2

        for i in range(low, low + k):
            compAndSwap(a_list, i, i + k, direction)
            display(a_list, fig)
        display(a_list, fig)
        bitonicMerge(a_list, low, k, direction, fig)
        bitonicMerge(a_list, low + k, k, direction, fig)


def bitonicSort(
    a_list,
    low,
    center,
    direction, fig
    ):

    if center > 1:
        k = center // 2
        bitonicSort(a_list, low, k, 1, fig)
        bitonicSort(a_list, low + k, k, 0, fig)
        bitonicMerge(a_list, low, center, direction, fig)
    return a_list


def bitonic_sort(a_list, fig):
    up = 1
    a_list = bitonicSort(reform(a_list), 0, len(a_list), up, fig)
    return a_list

# Stooge Sort
def stooge_sort_run(a_list, low, high, fig):
    if low >= high:
        return a_list

    if a_list[low] > a_list[high]:
        (a_list[low], a_list[high]) = (a_list[high], a_list[low])
        display(a_list, fig)

    if high - low > 1:
        t = (high - low + 1) // 3

        stooge_sort_run(a_list, low, high - t, fig)
        stooge_sort_run(a_list, low + t, high, fig)
        stooge_sort_run(a_list, low, high - t, fig)
    return a_list


def stooge_sort(a_list, fig):
    low = 0
    high = len(a_list) - 1
    a_list = stooge_sort_run(a_list, low, high, fig)
    return a_list

# Radix Sort

def rcounting_sort(a_list, max_value, get_index):
    counts = [0] * max_value

    for a in a_list:
        counts[get_index(a)] += 1
    for (i, c) in enumerate(counts):
        if i == 0:
            continue
        else:
            counts[i] += counts[i - 1]
    for (i, c) in enumerate(counts[:-1]):
        if i == 0:
            counts[i] = 0
        counts[i + 1] = c
    ret = [None] * len(a_list)

    for a in a_list:
        index = counts[get_index(a)]
        ret[index] = a
        counts[get_index(a)] += 1
    # display(a_list)
    return a_list


def get_digit(n, d):
    for i in range(d - 1):
        n //= 10
    return n % 10


def get_num_digit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def check_digits(a_list):
    cnt = 0
    for i in range(len(a_list)):
        if a_list[i] % 10 == a_list[i]:
            cnt += 1
        else:
            cnt = 0
    if cnt == len(a_list):
        return True
    else:
        return False


def radix_sort(a_list, fig):
    flag = check_digits(a_list)
    if flag:
        a_list.append(10)
    max_value = max(a_list)
    num_digits = get_num_digit(max_value)

    for d in range(num_digits):
        a_list = rcounting_sort(a_list, max_value, lambda a: \
                               get_digit(a, d + 1))
        # display(a_list)
    if flag:
        a_list.remove(10)
    return a_list

# Tim Sort
def TimInsertionSort(a_list, left, right, fig):
    for i in range(left + 1, right):
        temp = a_list[i]
        j = i - 1

        while a_list[j] > temp and j >= left:
            a_list[j + 1] = a_list[j]
            display(a_list, fig)
            j -= 1
        a_list[j + 1] = temp


def merge(
    a_list,
    l,
    m,
    r, fig
    ):

    len1 = m - l + 1
    le2 = r - m

    left = [0] * len1
    right = [0] * len2

    for i in range(len1):
        left[i] = a_list[l + i]

    for i in range(len2):
        right[i] = a_list[m + 1 + i]

    i = 0
    j = 0
    k = 0

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j += 1
        k += 1
    display(a_list, fig)
    while i < len1:
        a_list[k] = left[i]
        k += 1
        i += 1
    display(a_list, fig)
    while j < len2:
        a_list[k] = right[j]
        k += 1
        j += 1
    display(a_list, fig)

def min(a, b):
    if a < b:
        return a
    else:
        return b


def timsort_run(a_list, n, fig):
    run = 32
    for i in range(0, n, run):
        TimInsertionSort(a_list, i, min(i + 31, n - 1), fig)

    size = run
    left = 0

    while size < n:
        while left < n:
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)

            merge(a_list, left, mid, right, fig)
            left += 2 * size
        size *= 2


def timsort(a_list, fig):
    size = len(a_list) + 1
    timsort_run(a_list, size, fig)
    return a_list

# Binary Insertion Sort
def binarySearch(
    a_list,
    val,
    start,
    end,
    ):

    if start == end:
        if a_list[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if a_list[mid] > val:
        return binarySearch(a_list, val, start, mid - 1)
    elif a_list[mid] < val:
        return binarySearch(a_list, val, mid + 1, end)
    else:
        return mid


def binary_insertion_sort(a_list, fig):
    for i in range(1, len(a_list)):
        val = a_list[i]
        j = binarySearch(a_list, val, 0, i - 1)
        a_list = a_list[:j] + [val] + a_list[j:i] + a_list[i + 1:]
        display(a_list, fig)

    return a_list

# Bucket Sort
def numberOfDigits(num):
    mdiv = num // 10
    mmod = mdiv % 10
    i = 1
    while mdiv != 0:
        mdiv = mdiv // 10
        mmod = mdiv % 10
        i += 1

    return i


def bucket_sort(a_list, fig):
    buckets = []
    for i in range(10):
        buckets.append([])
    
    for i in range(len(a_list)):
        h = numberOfDigits(a_list[i])
        buckets[h].append(a_list[i])
    #display(buckets)
    for i in range(10):
        buckets[i] = insertion_sort(buckets[i], fig)
    #display(buckets)
    j = 0
    for i in range(10):
        while buckets[i]:
            a_list[j] = buckets[i].pop(0)
            display(a_list, fig)
            j += 1

    return a_list

# Shell Sort
def gapInsertionSort(a_list, start, gap, fig):
    for i in range(start + gap, len(a_list), gap):

        currentValue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentValue:
            a_list[position] = a_list[position - gap]
            display(a_list, fig)
            position = position - gap

        a_list[position] = currentValue


def shell_sort(a_list, fig):
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount, fig)

        sublistcount = sublistcount // 2
    return a_list

# Cocktail Sort
def cocktail_sort(a_list, fig):
    swapped = False
    end = 0
    for k in range(len(a_list) - 1, end, -1):
        for i in range(k, 0, -1):
            if a_list[i] < a_list[i - 1]:
                (a_list[i], a_list[i - 1]) = (a_list[i - 1], a_list[i])
                x = display(a_list, fig)
                if x == -1:
                    x = 0
                    return a_list
                swapped = True

        for i in range(k):
            if a_list[i] > a_list[i + 1]:
                (a_list[i], a_list[i + 1]) = (a_list[i + 1], a_list[i])
                x = display(a_list, fig)
                if x == -1:
                    x = 0
                    return a_list
                swapped = True

        end = end + 1
        if not swapped:
            return
    return a_list

# Heap Sort
def heapify(a_list, count, fig):
    start = int((count - 2) / 2)
    while start >= 0:
        sift_down(a_list, start, count - 1, fig)
        start -= 1


def sift_down(a_list, start, end, fig):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if a_list[swap] < a_list[child]:
            swap = child
        if child + 1 <= end and a_list[swap] < a_list[child + 1]:
            swap = child + 1
        if swap != root:
            (a_list[root], a_list[swap]) = (a_list[swap], a_list[root])
            display(a_list, fig)
            root = swap
        else:
            return


def heap_sort(a_list, fig):
    heapify(a_list, len(a_list), fig)
    end = len(a_list) - 1
    while end > 0:
        (a_list[end], a_list[0]) = (a_list[0], a_list[end])
        display(a_list, fig)
        end -= 1
        sift_down(a_list, 0, end, fig)
    return a_list

# Gnome Sort
def gnome_sort(a_list, fig):
    i = 0
    while i < len(a_list):
        if i == 0 or a_list[i - 1] <= a_list[i]:
            i += 1
        else:
            (a_list[i], a_list[i - 1]) = (a_list[i - 1], a_list[i])
            x = display(a_list, fig)
            if x == -1:
                return a_list
            i -= 1
    return a_list

# Sleep Sort
def sleep_sort(a_list, fig):

    def sleepSort(i):

        sleep(i)
        a_list.append(i)

    threads = []
    for j in range(len(a_list)):
        t = threading.Thread(target=sleepSort, args=(a_list.pop(0), ))

        threads.append(t)
        t.start()
        display(a_list, fig)

    for i in range(len(threads)):

        display(a_list, fig)
        threads[i].join()
    return a_list

# Pancake Sort
def pancake_sort(a_list, fig):
    if len(a_list) <= 1:
        return a_list

    for size in range(len(a_list), 1, -1):
        maxindex = max(range(size), key=a_list.__getitem__)

        if maxindex + 1 != 0:
            a_list[:maxindex + 1] = reversed(a_list[:maxindex + 1])
            display(a_list, fig)
        a_list[:size] = reversed(a_list[:size])
        display(a_list, fig)
    return a_list

# Cycle Sort
def cycle_sort(a_list, fig):
    writes = 0

    for (cstart, item) in enumerate(a_list):

        pos = cstart
        for item2 in a_list[cstart + 1:]:
            if item2 < item:
                pos += 1

        if pos == cstart:
            continue

        while item == a_list[pos]:
            pos += 1
        (a_list[pos], item) = (item, a_list[pos])
        display(a_list, fig)
        writes += 1

        while pos != cstart:
            pos = cstart

            for item2 in a_list[cstart + 1:]:
                if item2 < item:
                    pos += 1

            while item == a_list[pos]:
                pos += 1

            (a_list[pos], item) = (item, a_list[pos])
            display(a_list, fig)
            writes += 1
    return a_list



			
