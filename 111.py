from sys import stdin

global aux

def lis_tab(a,b,N):
    #a = aux, b = ref
    ans = 0
    if N!=0:
        tab = [ None for i in range(N) ]
        for n in range(N):
            tab[n] = 0
            for i in range(n):
                if b[a[i]]<b[a[n]]:
                    tab[n] = max(tab[n],tab[i])
            tab[n] += 1
            ans = max(ans,tab[n])
    return ans

MAX = 30
tmp = [ None for i in range(MAX) ]
tmp2 = [ None for i in range(MAX) ]

def mergesort(a,low,hi):
    '''Merge-Sort algorithm for arrays of up to MAX elements'''
    global MAX
    # conquer phase: do nothing when a[low,hi) has 0 or 1 elements
    if low+1<hi:
        # divide phase: there are at least two elements in a[low,hi)
        mid = low+((hi-low)//2)
        mergesort(a,low,mid)        # solve left half
        mergesort(a,mid,hi)         # solve right half
        merge(a,low,mid,hi)         # merge left and right parts

def merge(a,low,mid,hi):
    global aux
    '''merge a[low,mid) and a[mid,hi) into a[low,hi) assumming
    that the two parts are sorted in ascending order'''
    global tmp,tmp2
    # copy a[low,hi) to tmp[low,hi)
    for k in range(low,hi):
        tmp[k] = a[k]
        tmp2[k] = aux[k]
    l,r,k = low,mid,low
    while k!=hi:
        if l==mid:
            # a[low,mid) has been processed
            aux[k] = tmp2[r]
            a[k] = tmp[r] ; r += 1
        elif r==hi:
            # a[mid,hi) has been processed
            aux[k] = tmp2[l]
            a[k] = tmp[l] ; l += 1
        else:
            # there are elements in each part to be processed
            if tmp[l] <= tmp[r]:
                aux[k] = tmp2[l]
                a[k] = tmp[l] ; l += 1
            else:
                aux[k] = tmp2[r]
                a[k] = tmp[r] ; r += 1
        k += 1

def main():
    global aux,tmp2
    entrada= [ int(x) for x in stdin.readline().strip().split() ]
    while len(entrada)!=0:
        if len(entrada)==1:
            N=entrada[0]
            refflag=True
        else:
            if refflag:
                ref=entrada[:]
                refflag=False
            else:
                aux = [ i for i in range(N) ]
                mergesort(entrada,0,N)
                print(lis_tab(aux,ref,N))
        entrada=[ int(x) for x in stdin.readline().strip().split() ]
main()


'''
Sample Input
4
4 2 3 1
1 3 2 4
3 2 1 4
2 3 4 1
10
3 1 2 4 9 5 10 6 8 7
1 2 3 4 5 6 7 8 9 10
4 7 2 3 10 6 9 1 5 8
3 1 2 4 9 5 10 6 8 7
2 10 1 3 8 4 9 5 7 6
Sample Output
1
2
3
6
5
10
9
'''
