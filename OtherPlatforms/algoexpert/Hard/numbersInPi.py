def numbersInPi(pi, numbers):
	DP={}
	preferred=set()
	for num in numbers:
		preferred.add(num)
		
	def DPphi(pi,n):
		nonlocal DP
		if n==len(pi):
			return -1
		check=DP.get(n)
		if check!=None:
			return check
		i=n
		ans=float("inf")
		while i<len(pi):
			if pi[n:i+1] in preferred:
				ans= min(1+DPphi(pi,i+1),ans)
			i+=1
		DP[n]=ans
		return ans
	
	ans=DPphi(pi,0)
	if ans==float("inf"):
		ans=-1
	return ans
	
    # Write your code here.
