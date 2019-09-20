def minNumberOfJumps(array):
   top=0
   steps=0
   newtop=float("-inf")

   i=0
   while(i<len(array)):
      if i>top:
         top=newtop
         steps+=1
      num=array[i]
      newtop=max(newtop,i+num)
      i+=1
   return steps

# Write your code here.
