class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            minm = i
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    minm = j
                    arr[i], arr[j] = arr[j], arr[i]

