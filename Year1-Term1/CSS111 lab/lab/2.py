num = input()
def func(num):
    num = [int(i) for i in num]
    for i in range(len(num)-1):
        if i % 2 == 0:
            if num[i] >= num[i+1]:
                return False
        else:
            if num[i] <= num[i+1]:
                return False
    else:
        return True

print(func(num))
