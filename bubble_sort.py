# It repeatedly visits the sequence to be sorted, comparing two elements at once, exchanging them if they are in the wrong order. The sequence of visits is repeated until no more exchanges are required, ie the sequence has been sorted.


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


aa = [2, 5, 1, 6, 7, 3, 9, 8, 0]

print(bubble_sort(aa))
