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