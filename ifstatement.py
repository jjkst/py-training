n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

print(n)

# and = &&
# or  = ||
n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    n += 1

print(n)