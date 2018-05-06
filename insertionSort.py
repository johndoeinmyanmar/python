def insertionSort(A):
	for j in range(1:len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			
