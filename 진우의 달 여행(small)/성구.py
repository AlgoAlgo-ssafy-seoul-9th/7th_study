# 진우의 달 여행 (Small)
'''
python 34176 KB 68 ms
'''
import sys
from collections import deque

input = sys.stdin.readline

# input
N, M = map(int, input().split())
fuel_mat = [list(map(int, input().split())) for _ in range(N)]

# define
dir = [(1, -1), (1, 0), (1, 1)]
min_fuel = 3601
visited = [[3601] * M for _ in range(N)]


# dfs 풀이
def dfs(y, x):
    global min_fuel
    # 초기값 설정
    stack = [(y, x, -1, fuel_mat[y][x])]
    while stack:
        i, j, preD, fuel = stack.pop()
        if i == N - 1:
            # 달에 도착하면 최소 연료 체크
            min_fuel = min(min_fuel, fuel)
            continue
        # 가지치기(이미 최소 연료를 넘어서면 넘김)
        if min_fuel <= fuel:
            continue
        # 방향 체크
        for idx in range(3):
            # 이미 지나온 방향이면 패스
            if idx == preD:
                continue
            # 갈 수 있는 방향 체크
            ni, nj = i + dir[idx][0], j + dir[idx][1]
            if 0 <= ni < N and 0 <= nj < M:
                stack.append((ni, nj, idx, fuel + fuel_mat[ni][nj]))


# 모든 곳에서 출발 가능
for m in range(M):
    dfs(0, m)

print(min_fuel)
""" 틀렸습니다
import sys
from collections import deque

input = sys.stdin.readline

# input
N, M = map(int, input().split())
fuel_mat = [list(map(int, input().split())) for _ in range(N)]

# define
dir = [(1, -1), (1, 0), (1, 1)]
min_fuel = 3601
visited = [[3601] * M for _ in range(N)]


def bfs(y, x):
    global min_fuel
    visited[y][x] = fuel_mat[y][x]
    que = deque([(y, x, -1)])
    while que:
        i, j, preD = que.popleft()
        if i >= N - 1:
            min_fuel = min(min_fuel, visited[i][j])
            continue
        for idx in range(3):
            if idx == preD:
                continue
            ni, nj = i + dir[idx][0], j + dir[idx][1]
            if 0 <= nj < M and 0 <= ni < N:
                visited[ni][nj] = min(visited[i][j] + fuel_mat[ni][nj], visited[ni][nj])
                que.append((ni, nj, idx))


# 최소 fuel 도착지 찾기
for m in range(M):
    bfs(0, m)
# for m in range(N):
#     print(*visited[m])

print(min_fuel)
"""
