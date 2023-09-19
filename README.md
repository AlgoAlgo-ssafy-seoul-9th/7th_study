# 7th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/16830)

[소프티어 문제](https://softeer.ai/practice/info.do?idx=1&eid=394)

<br><br><br>

# 우물 안 개구리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./우물 안 개구리/민웅.py>)

```py
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

W_lst = list(map(int, input().split()))

p_lst = [[] for _ in range(N+1)]

cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    p_lst[a].append(b)
    p_lst[b].append(a)

for i in range(N):
    temp = W_lst[i]
    for v in p_lst[i+1]:
        if W_lst[v-1] >= temp:
            break
    else:
        cnt += 1

print(cnt)

```

## [병국](<./우물 안 개구리/병국.py>)

```py
n,m = map(int,input().split())
arr = list(map(int,input().split()))

answer = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    if answer[a-1] == answer[b-1] == -1:
        pass
    elif answer[a-1] == -1 and answer[b-1] != -1:
        if arr[a-1] > arr[b-1]:
            answer[b-1] = -1
        elif arr[a-1] < arr[b-1]:
            answer[b-1] = 1
        else:
            answer[b-1] = -1
        answer[a-1] = -1
    elif answer[a-1] != -1 and answer[b-1] == -1:
        if arr[a-1] > arr[b-1]:
            answer[a-1] = 1
        elif arr[a-1] < arr[b-1]:
            answer[a-1] = -1
        else:
            answer[a-1] = -1
        answer[b-1] = -1
    elif answer[a-1] != -1 and answer[b-1] != -1:
        if arr[a-1] > arr[b-1]:
            answer[a-1] = 1
            answer[b-1] = -1
        elif arr[a-1] < arr[b-1]:
            answer[a-1] = -1
            answer[b-1] = 1
        else:
            answer[a-1] = -1
            answer[b-1] = -1
print(answer.count(1)+answer.count(0))
```

## [상미](<./우물 안 개구리/상미.py>)

```py

```

## [서희](<./우물 안 개구리/서희.py>)

```py

```

## [성구](<./우물 안 개구리/성구.py>)

```py
# 우물 안 개구리
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
weight_list = list(map(int, input().split()))

# define
friends = [[] for _ in range(N)]
cnt = 0

# input
for _ in range(M):
    a,b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

# logic
for i in range(N):
    # 친구가 있을때
    if friends[i]:
        # 친구들 중에
        for friend in friends[i]:
            # 나보다 무거운 무게치는 아이 있으면
            if weight_list[i] <= weight_list[friend]:
                # 멈춰
                break
        else:
            # 없으면 내가 짱임! count
            cnt += 1
    # 친구가 없을 때
    else:
        # 아무래도 내가 짱임! count
        cnt += 1
print(cnt)

```

</div>

</details>

<br><br><br>

# 진우의 달 여행(Small)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./진우의%20달%20여행(small)/민웅.py>)

```py
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
```

## [병국](<./진우의%20달%20여행(small)/병국.py>)

```py
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 방향
dir = [(1,1),(1,-1),(1,0)]
q = []
for _ in range(m):
    q.append((0,_,arr[0][_],-1))
answer = []
while q:
    x,y,cnt,check = q.pop(0)
    for i in range(len(dir)):
        cx = x+dir[i][0]
        cy = y+dir[i][1]
        if 0<=cx<n and 0<=cy<m and check != i:
            if cx == n - 1:
                answer.append(cnt + arr[cx][cy])
            else:
                q.append((cx,cy,cnt+arr[cx][cy],i))
print(min(answer))

```

## [상미](<./진우의%20달%20여행(small)/상미.py>)

```py

```

## [서희](<./진우의%20달%20여행(small)/서희.py>)

```py

```

## [성구](<./진우의%20달%20여행(small)/성구.py>)

```py
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
```

</div>

</details>

<br><br><br>

# 1의 개수 세기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./1의%20개수%20세기/민웅.py)

```py
# 9527_1의개수세기_howmanyone
# 시간초과
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

dp = [0]*(len(bin(10**16))-1)
dp[1] = 1
for i in range(2, 55):
    dp[i] = 2**(i-1) + 2*dp[i-1]

bA = len(bin(A))-2
bB = len(bin(B))-2
temp = 0
for i in range(2**(bB-1), B+1):
    # print(bin(i))
    temp += bin(i).count('1')
temp2 = 0
for i in range(A, 2**(bA-1)):
    # print(bin(i))
    temp2 += bin(i).count('1')
print(dp[bB-1] - dp[bA-1] + temp + temp2)


```

## [병국](./1의%20개수%20세기/병국.py)

```py

```

## [상미](./1의%20개수%20세기/상미.py)

```py

```

## [서희](./1의%20개수%20세기/서희.py)

```py

```

## [성구](./1의%20개수%20세기/성구.py)

```py

```

</div>

</details>

<br><br><br>

# 컨베이어 벨트 위의 로봇

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./컨베이어 벨트 위의 로봇/민웅.py>)

```py

```

## [병국](<./컨베이어 벨트 위의 로봇/병국.py>)

```py
from collections import deque

n, k = map(int,input().split())
arr = list(map(int,input().split()))
# 로봇의위치는 인덱스 0, 인덱스 n에 있음 현재
# 한칸씩 땡기는걸 어떻게하지
robot = deque([0]*(2*n))

answer = deque(arr)
real_cnt = 0
while True:
    # 1번 사이클
    answer.rotate(1)
    robot.rotate(1)

    # 끝에있으면 내리기
    robot[n-1] = 0

    # 2번 사이클
    for bb in range(n-2,-1,-1):
        if robot[bb] == 1 and robot[bb+1] != 1 and answer[bb+1] >= 1:
            robot[bb] = 0
            robot[bb+1] = 1
            answer[bb+1] -= 1
    robot[n-1] = 0
    # 3번 사이클
    if robot[0] == 0 and answer[0] != 0:
        robot[0] = 1
        answer[0] -= 1
    real_cnt += 1
    # 4번 사이클
    cnt = 0
    if answer.count(0) >= k:
        print(real_cnt)
        break

        # 로봇위치 체크해서

        # robot[]
# [0,1,2,3,4]
# [4,0,1,2,3]
# arr = arr[]
# 2N 내리고 1 올리고 , N 내리고 N+1 올리고
# 로봇은 올리는 위치에만 올릴수있고, 로봇이 내리는 위치에 도달하면 즉시 내림

#1로봇 2 1
#2    1 2로봇

# 첫번째 싸이클에서
# 2 1로봇 2
# 1 2로봇 1 이 되고

# 두번째 사이클에서
# 2         0 1(로봇내림)
# 0(로봇내림) 1 1

# 세번째 사이클에서
# 1(로봇올림) 0 1
# 0         1 0(로봇올림)
```

## [상미](<./컨베이어 벨트 위의 로봇/상미.py>)

```py

```

## [서희](<./컨베이어 벨트 위의 로봇/서희.py>)

```py

```

## [성구](<./컨베이어 벨트 위의 로봇/성구.py>)

```py
# 20055 컨베이어 벨트 위의 로봇
"""
python 31256 KB 4168 ms
pypy   115432KB  312 ms
"""

import sys

input = sys.stdin.readline

# input
N, K = map(int, input().split())

A_list = list(map(int, input().split()))

# define
# 로봇 위치
robot = [0] * (2 * N)
# 컨베이어 벨트 로봇 놓는 곳
start = 0
# 컨베이어 벨트 로봇 빼는곳
end = N - 1
# 턴수
cnt = 1
# 0이 된 index
zero = set()

while True:
    # 컨베이어 벨트 이동
    start = start - 1 if start else 2 * N - 1
    end = end - 1 if end else 2 * N - 1
    # end위치에 있는 로봇을 뺌
    robot[end] = 0
    # 로봇 이동
    for i in range(N - 1, -1, -1):
        # 로봇을 발견하면
        if robot[(start + i) % (2 * N)]:
            # 바로 앞에 로봇이 없고 내구도가 있는가?
            if (
                A_list[(start + 1 + i) % (2 * N)]
                and not robot[(start + i + 1) % (2 * N)]
            ):
                # 그곳이 end 위치인가?
                if (start + 1 + i) % (2 * N) == end:
                    # end 위치면 뺌
                    robot[(start + i) % (2 * N)] = 0
                # end 아니면 이동 표시
                else:
                    robot[(start + i) % (2 * N)], robot[(start + i + 1) % (2 * N)] = (
                        0,
                        1,
                    )
                # 내구도 깍임
                A_list[(start + 1 + i) % (2 * N)] -= 1
                # 내구도가 0이 됬는지 체크, 됬으면 zero에 추가
                if not A_list[(start + 1 + i) % (2 * N)]:
                    zero.add((start + 1 + i) % (2 * N))
    # 내구도가 있는 곳이면 로봇 놓기
    if A_list[start]:
        # 로봇 표시
        robot[start] = 1
        # 내구도 깍임
        A_list[start] -= 1
        # 내구도 0 체크
        if not A_list[start]:
            zero.add(start)
    # 내구도 0인 곳 개수가 K개인가?
    if len(zero) >= K:
        break
    # 턴 ++
    cnt += 1
print(cnt)

```

</div>

</details>

<br><br><br>
