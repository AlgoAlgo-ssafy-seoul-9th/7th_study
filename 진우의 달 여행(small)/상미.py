## 백준 17484 _ 진우의 달 여행

def sol(x, y, fuel):
    if x == N-1:
        return fuel
    elif 0 <= x <= N-2:
        if 0 <= y-1:
            sol(x +1, y -1, fuel + arr[x+1][y-1])
        elif y+1 <= M-1: 
            sol(x +1, y+1, fuel + arr[x+1][y+1])
        sol(x +1, y, fuel + arr[x+1][y])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [(1, -1), (1, 0), (1, 1)]
lst = []

for i in range(M):
    lst.append(sol(0, i, 0))

print(lst)