import io
import sys

_INPUT = """\
6
10
.|..*...|.
10
.|..|.*...
3
|*|
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  ans=0
  for i in range(N):
    if S[i]=='|': ans^=1
    elif S[i]=='*': break
  print('out' if ans==0 else 'in')