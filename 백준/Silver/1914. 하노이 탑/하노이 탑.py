def tower_of_hanoi(A, B, n):
    if n == 1:
        print(A, B)
        return

    tower_of_hanoi(A, 6-A-B, n-1) #1단계 (1->2)
    print(A, B) #2단계 (마지막 원판 1->3)
    tower_of_hanoi(6-A-B, B, n-1) #3단계 (2->3)

n = int(input())
print(2**n-1)
if n <= 20:
    tower_of_hanoi(1,3,n)