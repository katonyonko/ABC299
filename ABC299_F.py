import io
import sys

_INPUT = """\
3
ababbaba
zzz
ppppqqppqqqpqpqppqpqqqqpppqppq
"""

def solve(test):
  S=input()
  mod=998244353
  inf=1<<30
  sigma=[inf]*(26*(len(S)+1))
  def idx(a,i): return a*(len(S)+1)+i
  def num(a): return ord(a)-ord('a')
  for i in range(len(S)):
    now=i
    while now>=0 and sigma[idx(num(S[i]),now)]==inf:
      sigma[idx(num(S[i]),now)]=i
      now-=1
  # print(sigma)
  ans=0
  for i in range(len(S)-1):
    #前i+1文字と後len(S)-i-1文字に分ける
    if sigma[idx(num(S[i+1]),0)]>=i+1: continue
    else:
      s=sigma[idx(num(S[i+1]),0)]
      def idx2(j,k): return j*(len(S)-i-1)+k
      dp=[0]*(i+1)*(len(S)-i-1)
      dp[idx2(s,0)]=1
      for j in range(i+1):
        for k in range(len(S)-i-1):
          if sigma[idx(num(S[i+1]),j+1)]==i+1:
            ans+=dp[idx2(j,k)]
            ans%=mod
          for l in range(26):
            if sigma[idx(l,j+1)]<i+1 and sigma[idx(l,i+k+2)]<len(S):
              dp[idx2(sigma[idx(l,j+1)],sigma[idx(l,i+k+2)]-i-1)]+=dp[idx2(j,k)]
              dp[idx2(sigma[idx(l,j+1)],sigma[idx(l,i+k+2)]-i-1)]%=mod
  if test==0:
    print(ans)
  else:
    return ans

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)