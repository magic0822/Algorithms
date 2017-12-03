# Hill Sort (Shell Sort) is a sort of insertion. Also known as reduced incremental sorting, is a more efficient and improved version of the direct insertion sort algorithm. Hill sort is a non-stable sorting algorithm. The method due to DL. Shell in 1959 made its name. Hill sorting is to record a certain increment according to the sub-group, the use of direct insertion sort algorithm for each group sort; As the incremental decrease, each group contains more and more keywords, when the increment is reduced to 1, The entire file is divided into groups, and the algorithm terminates.


def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


aa = [2, 5, 1, 6, 7, 3, 9, 8, 0]

print(shell_sort(aa))
