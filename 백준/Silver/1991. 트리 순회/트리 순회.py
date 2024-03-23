import sys

# sys.setrecursionlimit(10**8)  # 재귀 호출의 깊이 제한을 늘림
# (트리의 깊이에 비례하여 메모리를 사용하므로, 
# 트리의 크기가 커지더라도 충분한 재귀 호출이 가능하도록)
# but, 권장되는 방법 아님.

cnt = int(sys.stdin.readline())

# 딕셔너리로 트리 구현
tree = {}
for i in range(cnt):
    root, left, right = map(str, sys.stdin.readline().split())  # 루트, 왼쪽자식, 오른쪽 자식
    tree[root] = left, right  # {'A': ('B', 'C')}


def preorder(node):  # 전위순회
    if node != ".":  # 루트 노트가 .이 아니면 (자식이 있다면)
        print(node, end="")
        preorder(tree[node][0])  # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[node][1])  # 재귀적으로 오른쪽 노드 탐색


def inorder(node):  # 중위순회
    if node != ".":  # .이 아니면
        inorder(tree[node][0])  # 재귀적으로 왼쪽 노드 탐색
        print(node, end="")  # 루트 노드 출력
        inorder(tree[node][1])  # 재귀적으로 오른쪽 노드 탐색


def postorder(node):  # 후위순회
    if node != ".":  # .이 아니면
        postorder(tree[node][0])  # 재귀적으로 왼쪽 노드 탐색
        postorder(tree[node][1])  # 재귀적으로 오른쪽 노드 탐색
        print(node, end="")  # 루트 노드 출력

# 루트노드: 'A'
preorder('A')
print("")
inorder('A')
print("")
postorder('A')