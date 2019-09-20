def largestRange(array):
	if len(array)==0:
		return [-1,-1]
	bestl=array[0]
	bestr=array[0]
	bestlength=1
	dic={}
	
	for num in array:
		check=dic.get(num)
		if check!=None:
			continue
		endl=num
		endr=num
		length=1
		
		left,right=num-1,num+1
		
		check=dic.get(left)
		if check!=None:
			length=check[2]+length
			endl=check[0]
			dic[left][2]=length
			dic[left][1]=endr
			
		check=dic.get(right)
		if check!=None:
			length=check[2]+length
			endr=check[1]
			dic[right][2]=length
			dic[right][0]=endl
			
		if length>bestlength:
			bestl=endl
			bestr=endr
			bestlength=length
		
		
		dic[num]=[endl,endr,length]
		dic[endl][2]=length
		dic[endl][1]=endr
		dic[endr][2]=length
		dic[endr][0]=endl
		
	return [bestl,bestr]
		
		
		
    # Write your code here.
