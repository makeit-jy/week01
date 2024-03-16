word_list = input().split()
reverse_a = word_list[0][::-1]
reverse_b = word_list[1][::-1]
print(max(int(reverse_a), int(reverse_b)))