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
