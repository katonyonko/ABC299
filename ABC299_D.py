import io
import sys

_INPUT = """\
6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  l,r=1,N
  while r-l>1:
    mid=(l+r)//2
    print('?',mid)
    S=int(input())
    if S==0: l=mid
    else: r=mid
  print('!',l)