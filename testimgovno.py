def sum_range(start, end) -> int:
    sum = 0
    if start > end:
        for i in range(end, start + 1, 1):
            sum += i
    else:
        for i in range(start, end + 1, 1):
            sum += i
    return sum

print(sum_range(10,2))