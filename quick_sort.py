# By sorting the data to be sorted into two separate parts, one part of all the data than the other part of all the data is small, and then press this method for the two parts of the data were quickly sorted, the entire sorting process can Recursive, in order to achieve the entire data into an orderly sequence.


def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while[left] < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
