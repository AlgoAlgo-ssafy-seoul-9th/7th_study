dxy = [(-1, 1), (0, 1), (1, 1)]

N,M = map(int, input().split())

space =  []
for _ in range(N):
    space.append(list(map(int, input().split())))
    
MinF = 100*N*M
for i in range(M):
    temp = 0
    for j in range(N):
        temp += space[i][j]
        for d in dxy:
            nx = i + d[0]
            ny = j + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                temp += space[nx][ny]
                if temp > MinF:
                    break
    if MinF > temp:
        MinF = temp
        
print(MinF)