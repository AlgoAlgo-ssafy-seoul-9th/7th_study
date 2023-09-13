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
