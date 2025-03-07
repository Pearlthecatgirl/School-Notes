
## Week 2 (Lecture 1)

### Searching

#### Binary search

- Searches for an integer, target in an ordered list
- Can be implemented recursively
    1. Define a midpoint, that is the middle element of a sorted array. 
    2. Check if the element is greater or lesser
        1. if greater, search from mid+1 to highest
        2. if lower, search from mid-1 to lowest
    3. repeat until you get to the final element
        1. if that element is equal, ret true
        2. else return false

### Sorting

#### Insertion sort

- Given an unsorted array, sort it by creating 2 portions of the array, the sorted and the unsorted portion.
- Over time, the sorted portion's size gets increased
- Iterate over the loop, and insert the current element into the 'left', the sorted portion of the array. 

- Example implementation

```
def insertion_sort(my_array:list):
    for element_n in range(1,len(my_array)):
        cur=my_array[element_n]
        countdown=element_n
        while (countdown>0) and (my_array[countdown-1] > cur):
            my_array[countdown]=my_array[countdown-1]
            countdown-=1
        my_array[countdown]=cur
```

#### Complexity of Insertion sort

- When doing complexity analysis, we must consider the worst-case complexity
    - There is no surprise to consider the worst
    - There is also a way to generate the *average case complexity* but you must know the underlying distribution to obtain the average.

- In the case of insertion sort (Asymptotic complexity):
    - we pretend the test arrary is very large, and that we don't know the size beforehand, so there is little to no difference between n and n-1 (e.g: 999999 is as large as 1000000)
    - We replace every case of 'n, n-1, n-2...' with n itself.
    - The complexity of a single insertion operation depends on 2 things:
        - How far is the element from the start of the array 
        - How far we have to move it to get it into the correct position

##### Claim:

- Since the length of the array is n, we have to do n comparisons for the insertion operation, we can say each takes *n* time
    - So the total time is $n\times n=n^{2}$

##### However...

- We don't do *n* work for each insertion, there is 1 comparison for the 2nd element, and 2 for the third element, $(n-1)$ comparisons for the last element
- Therefore, the total work is actually:

$1 + 2 + 3 + ... + (n-1)=\frac{n(n-1)}{2}=\frac{n^2}{2}-\frac{n}{2}$

##### However...

Due to different steps/complexities in different languages/architecture, and removing the constant, we simply consider the complexity:

$n^{2}$

###### In big o notation:

$O\left(n^{2}\right)$






