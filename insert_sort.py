# The basic operation of insertion sorting is to insert a data into the ordered data which has already been sorted, and get a new, the number plus one of the ordered data, the algorithm is suitable for small data sorting, the time complexity is O ( N ^ 2). Is a stable sorting method. The insertion algorithm divides the array to be sorted into two parts: the first part contains all the elements of the array, except for the last element (leaving the array more than one space to insert), and the second part contains only this element (Ie, elements to be inserted). After the first part of the sort is complete, and then insert the final element of the first part has been arranged in the order.


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


aa = [2, 5, 1, 6, 7, 3, 9, 8, 0]

print(insert_sort(aa))
