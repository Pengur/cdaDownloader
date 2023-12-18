import sys

print(sys.argv)
it = iter(sys.argv)
for x, y in zip(it, it):
    print(x, y)
