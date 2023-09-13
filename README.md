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

```

## [병국](<./진우의%20달%20여행(small)/병국.py>)

```py

```

## [상미](<./진우의%20달%20여행(small)/상미.py>)

```py

```

## [서희](<./진우의%20달%20여행(small)/서희.py>)

```py

```

## [성구](<./진우의%20달%20여행(small)/성구.py>)

```py

```

</div>

</details>

<br><br><br>

# 1의 개수 세기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./1의%20개수%20세기/민웅.py>)

```py

```

## [병국](<./1의%20개수%20세기/병국.py>)

```py

```

## [상미](<./1의%20개수%20세기/상미.py>)

```py

```

## [서희](<./1의%20개수%20세기/서희.py>)

```py

```

## [성구](<./1의%20개수%20세기/성구.py>)

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

```

## [상미](<./컨베이어 벨트 위의 로봇/상미.py>)

```py

```

## [서희](<./컨베이어 벨트 위의 로봇/서희.py>)

```py

```

## [성구](<./컨베이어 벨트 위의 로봇/성구.py>)

```py

```

</div>

</details>

<br><br><br>
