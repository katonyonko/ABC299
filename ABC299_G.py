import io
import sys

_INPUT = """\
6
4 3
2 3 1 3
4 4
2 3 1 4
20 10
6 3 8 5 8 10 9 3 6 1 8 3 3 7 4 7 2 7 8 5
7 4
2 4 3 4 2 3 1
8 4
1 2 1 3 1 3 4 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  class SegTree:
    X_unit = 1 << 30
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def get_val(self,idx):
        return self.X[idx+self.N]

  N,M=map(int,input().split())
  A=list(map(lambda x: int(x)-1,input().split()))
  cnt=[0]*M
  ans=[]
  st=SegTree(N)
  st.build(A)
  d=defaultdict(list)
  for i in range(N):
    cnt[A[i]]+=1
    d[A[i]].append(i)
  l=0
  s=set()
  for i in range(N):
    cnt[A[i]]-=1
    if cnt[A[i]]==0 and A[i] not in s:
      while l<=i:
        tmp=st.fold(l,i+1)
        ans.append(tmp)
        s.add(tmp)
        if len(ans)==M: break
        while A[l]!=tmp: l+=1
        l+=1
        for j in d[tmp]: st.set_val(j,1<<30)
        if A[i]<=tmp: break
  print(*[ans[i]+1 for i in range(M)])