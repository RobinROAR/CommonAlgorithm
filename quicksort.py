#Edit by Robin
#2014.12.8
#快速排序的实现

#挖坑方法
def quicksort(A):
	size = len(A)
	key = A[0]
	i=0
	j=size-1
	while(i!=j):
		print "j = %d" % (j)
		if (A[j]<=key):
			A[i]=A[j]
			i+=1
			while(i<j):
				print "i = %d" % (i)
				if(A[i]>key):
					A[j] = A[i]
					j-=1
					break
				i+=1
			continue
		j-=1
	print key
	#最后填坑
	A[i] = key	
	print A
	#递归过程，三种情况
	if (i>0):
		A[:i] = quicksort(A[:i])
		if (i<size-1):
			A[i+1:] = quicksort(A[i+1:])
	if (i==0 and size>1):
		A[i+1:] = quicksort(A[i+1:])
	
	return A

#调试用模块
if __name__ == "__main__":
	a = [8,9,4,2,6,7,1,3,0]
	print quicksort(a)




