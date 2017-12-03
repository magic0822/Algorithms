# The basic idea: the first trip, to be sorted records r1 ~ r [n] select the smallest record, it and r1 exchange; the second trip, to be sorted records r2 ~ r [n] select the smallest record , It is exchanged with r2; and so on, the i-th track selects the smallest record among the records r [i] ~ r [n] to be sorted, exchanges it with r [i], and causes the ordered sequence to grow until All sorted.


def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > list[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists
