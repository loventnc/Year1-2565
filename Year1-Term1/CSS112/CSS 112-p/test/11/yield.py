def lo(nums):
    n = 0
    for i in range(nums):
        n = n+1
        yield n

ve = lo(10)

for i in ve:
    print(i)

print(list(lo(10)))