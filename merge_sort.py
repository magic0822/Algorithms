# Merge sorting is an effective sorting algorithm based on merging operations, which is a very typical application of Divide and Conquer. The ordered subsequences are merged to obtain a completely ordered sequence; that is, each sub-sequence is ordered, and then the subsequences are ordered. If the two order form into a sorted list, known as the two-way merge. In this case,
#
# The process of merging is to compare the size of a [i] and a [j], if a [i] ≤a [j], the elements a [i] in the first sorted list are copied into r [k] , And let i and k respectively add 1; otherwise the second order in the table elements a [j] copied to r [k], and j and k were added 1, so cycle down until An ordered list is taken, and then the remaining elements of the other ordered list are copied into the unit of r from subscript k to subscript t. Merge sorting algorithm We usually use the recursive implementation, first to be sorted interval [s, t] to the midpoint of the two points, and then the left sub-interval sort, then the right sub-interval sort, and finally left and right interval interval with a merge operation Merged into ordered intervals [s, t].


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[:num])
    return merge(left, right)
