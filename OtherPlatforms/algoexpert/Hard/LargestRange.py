'''
Largest Range

Write a function that takes in an array of integers and returns an array
of length 2 representing the largest range of numbers contained in that
array. The first number in the output array should be the first number
in the range while the second number should be the last number in the range.
A range of numbers is definced as a set of numbers that come right after each
other in the set of real integers. For instance, the output array [2,6]
represents the range {2,3,4,5,6}, which is a range of length 5. Note that the
numbers do not need to be ordered or adjacent in the array in order to form
a range. Asuume that there will only be one largest range.
'''

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
