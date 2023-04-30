import io
import sys

_INPUT = """\
6
5 5
1 2
2 3
3 1
3 4
4 5
2
1 0
5 2
5 5
1 2
2 3
3 1
3 4
4 5
5
1 1
2 1
3 1
4 1
5 1
1 0
0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  K=int(input())
  cond=[]
  for _ in range(K):
    p,d=map(int,input().split())
    p-=1
    cond.append((p,d))
  if K==0:
    print('Yes')
    print('1'*N)
  else:
    dist=[bfs(G,i) for i in range(N)]
    ans=['1']*N
    for i in range(K):
      p,d=cond[i]
      for j in range(N):
        if dist[p][j]<d: ans[j]='0'
    flg=0
    if '1' not in ans: flg=1
    if flg==0:
      for i in range(K):
        p,d=cond[i]
        if min([dist[p][j] for j in range(N) if ans[j]=='1'])!=d:
          flg=1
    if flg==0:
      print('Yes')
      print(*ans,sep='')
    else:
      print('No')