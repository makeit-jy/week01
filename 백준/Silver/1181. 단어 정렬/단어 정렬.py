import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().strip())
    
set_ = set(word_list)
word_list = list(set_)
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)