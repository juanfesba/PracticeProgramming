from sys import stdin

def lis_tab(a):
  ans,N = 0,len(a)
  if N!=0:
    tab = [ None for i in range(N) ]
    for n in range(N):
      tab[n] = 0
      for i in range(n):
        if a[i]>=a[n]:
          tab[n] = max(tab[n],tab[i])
      tab[n] += 1
      ans = max(ans,tab[n])
  return ans

def main():
    entrada=int(stdin.readline())
    i=1
    flag=False
    while entrada!=-1:
        if flag:
            print()
        flag=True
        misil=[entrada]
        entrada=int(stdin.readline())
        while entrada!=-1:
            misil.append(entrada)
            entrada=int(stdin.readline())
        print('Test #{}:'.format(i));
        print('  maximum possible interceptions: {}'.format(lis_tab(misil)))
        i+=1
        entrada=int(stdin.readline())

main()
