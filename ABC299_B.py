import io
import sys

_INPUT = """\
6
4 2
1 2 1 2
6 3 4 5
4 2
1 3 1 4
6 3 4 5
2 1000000000
1000000000 1
1 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,T=map(int,input().split())
  C=list(map(int,input().split()))
  R=list(map(int,input().split()))
  if T in C:
    m=max([R[i] for i in range(N) if C[i]==T])
  else:
    m=max([R[i] for i in range(N) if C[i]==C[0]])
  print(R.index(m)+1)