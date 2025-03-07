#!/usr/bin/python3
# Insertion sort
def insertion_sort(array:list): 
    current = array[0]
    for element in range(len(array)-1):
        if array[element+1]<array[element]:
            tmp=array[element+1]
            i=element
            while tmp>array[i]:
                array[i]=array[i-1]
                if (i==0):
                    continue
                i-=1

a=[5,2,4,6]
insertion_sort(a)
print(a)



