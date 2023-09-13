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