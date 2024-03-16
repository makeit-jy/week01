import math

a, b, v = map(int, input().split())
h = (v-b)/(a-b)
print(math.ceil(h))