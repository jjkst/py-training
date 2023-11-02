# regular vs generator
def first_n(n):
    '''Build and return a list'''
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sum(first_n(1000000)))

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(1000000)))
