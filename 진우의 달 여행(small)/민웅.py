# 17484_진우와달여행_traveltomoon
import sys
input = sys.stdin.readline
dxy = [(1, 0), (1, -1), (1, 1)]

def bt(si, sj):
    global ans
    global field

    stack = [[si, sj, field[si][sj], 3]]
    while stack:
        x, y, gas, idx = stack.pop()
        if x == N-1:
            if gas < ans:
                ans = gas
        else:
            for j in range(3):
                if j != idx:
                    dx = x + dxy[j][0]
                    dy = y + dxy[j][1]
                    if 1 <= dx <= N-1 and 0 <= dy <= M-1:
                        stack.append([dx, dy, gas+field[dx][dy], j])


N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
field.append([0]*M)

ans = float('inf')

for i in range(M):
    bt(0, i)

print(ans)