def minRewards(scores):
	if len(scores)==1:
		return 1
	sum=0
	last=scores[0]
	laststate=0
	count=1
	lasttop=float("inf")
	i=1
	while i<len(scores):
		cur=scores[i]
		if last>cur: #1 down
			if laststate==2:
				sum+=(count*(count+1))/2
				lasttop=count
				count=0
				sum=int(sum)
			laststate=1
			count+=1
		else: #last<cur up
			if laststate==1:
				sum+=(count*(count+1))/2-1
				if lasttop<=count:
					sum+=abs(lasttop-count)+1
				sum=int(sum)
				count=1
				
			laststate=2
			count+=1
		last=cur
		i+=1
	if laststate==1:
		sum+=(count*(count+1))/2
		if lasttop<=count:
			sum+=abs(lasttop-count)+1
		sum=int(sum)
	else:
		if laststate==2:
			sum+=(count*(count+1))/2
			count=0
			lasttop=count
			sum=int(sum)
	return sum
    # Write your code here.
