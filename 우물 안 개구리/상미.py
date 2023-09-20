## 소프티어_ 우물 안 개구리

N, M = map(int, input().split())
weight = list(map(int, input().split()))
friend = []
for _ in range(M):
    friend.append(list(map(int, input().split())))

# 1) weight[i] 가 weight[friend에서 i와 쌍을 이루는 수] 중 제일 크면 cnt+1
# 2) i가 friend에 아예 없으면 cnt+1

cnt = 0
for i in range(N):
    comp = []
    for [x, y] in friend:
        if x == i:
            comp.append(weight[y-1])
        if y == i:
            comp.append(weight[x-1])
    if comp:
        if max(comp) < weight[i-1]:
            cnt += 1
cnt_c = 0
for i in range(N):
    for f in friend:
        if i not in f:
            cnt_c += 1
    if cnt_c == M:
        cnt += 1
print(cnt)