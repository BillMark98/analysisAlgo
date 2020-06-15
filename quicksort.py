import random
import numpy as np
Factor = 19
class QuickSort:
    def __init__(self):
        pass

    def partition(self,arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 

        for j in range(low , high): 
    
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
    
    # Function to do Quick sort 
    def quickSort(self,arr,low,high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            quickSort(arr, low, pi-1) 
            quickSort(arr, pi+1, high) 
    
    def partitionCountXchange(self, arr,low,high):
        i = low
        pivot = arr[high]
        j = high - 1
        exchange = 0
        while (True):
            while (i < high and arr[i] < pivot) :
                i += 1
            while (j >= low and arr[j] > pivot) :
                if (j == low):
                    break
                j -= 1
            if (i < j) :
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
                exchange += 1
            else :
                break
        return exchange

    def xchangeArr(self,sizeArr, runTime):

        sumExchange = 0
        for i in range(runTime):
            array = random.sample(range(sizeArr * 10), sizeArr)
            sumExchange += self.partitionCountXchange(array,0,sizeArr - 1)
        return sumExchange / runTime

    def xchangeSimulate(self, testTime):
        sizeArr = [int(i * Factor) for i in np.linspace(1,10,testTime)]
        xchange = [None] * testTime
        for i in range(len(sizeArr)):
            arrsize = sizeArr[i]
            shouldVal = (arrsize - 2)/6
            xchange[i] = [self.xchangeArr(arrsize,arrsize * arrsize),shouldVal]

        print("N".rjust(10), "experiment data".rjust(20), "theoretical".rjust(20))
        for arrsize, data in zip(sizeArr,xchange):
            print("{0:10d} {1:20.6f} {2:20.6f}".format(arrsize, data[0],data[1]))
            # print(arrsize,data[0],data[1])


mysort = QuickSort()
array = random.sample(range(20), 10)
print(array)
mysort.xchangeSimulate(4)
# print(mysort.partitionCountXchange(array,0,9))

a = 2
b = 3
# print("{}")


# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
