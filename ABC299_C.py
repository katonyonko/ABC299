import io
import sys

_INPUT = """\
6
10
o-oooo---o
1
-
30
-o-o-oooo-oo-o-ooooooo--oooo-o
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  now=0
  tmp=0
  ans=[]
  for i in range(N):
    if (S[i]=='o')&(now==1) or (S[i]=='-')&(now==0):
      tmp+=1
    else:
      ans.append(tmp)
      now^=1
      tmp=1
  ans.append(tmp)
  t=[ans[2*i+1] for i in range(len(ans)//2) if ans[2*i]>0 or 2*i+2<len(ans) and ans[2*i+2]>0]
  if len(t)>0: print(max(t))
  else: print(-1)