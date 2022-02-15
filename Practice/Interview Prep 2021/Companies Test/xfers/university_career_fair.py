def universityCareerFair(arrival, duration):

    intervals = list(zip(arrival, duration))
    aux = sorted(
        intervals,
        key=lambda p: p[1]) # sort by arrival time, then duration
    )
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end: # if we can fit in the current interval
            ans, end = ans + 1, arr + dur
    return ans



print(universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])) # 4
print(universityCareerFair([1, 2], [7, 3])) # 1
print(universityCareerFair([1, 3, 4, 6], [4, 3, 3, 2])) # 2
 