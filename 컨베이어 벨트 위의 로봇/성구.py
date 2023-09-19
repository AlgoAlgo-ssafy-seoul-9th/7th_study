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
