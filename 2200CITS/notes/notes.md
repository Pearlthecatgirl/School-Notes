## Week 2 (Lecture 1)

### Searching

## Week 2 (Lecture 2)

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

#### Merge Sort

- A worst case complexity of $O\left(n\times log\left(n\right)\right)$
- Based on divide and conquer of array.

#### Complexity of Merge Sort

### Static Determination vs runtime Determination

- The memory requirement of a *recursive* function/method is unknown at compile time.
    - Therefore, memory for each function call is dynamically allocated
    - At each call, more memory is allocated on the stack for that call.
        - If there is a large amount of recursive calls, there will be a lot of memory required just to handle the function calls.

#### Complexity Analysis

- Running time grows with input size
    - Average case is too difficult to determine
    - Consider the worst case scenario
    - log is usually base-2
    - complexity cannot be lower than 10

##### Big O notation

- Given functions $f\left(n\right)$ and $g\left(n\right)$, we say that 

$$
f\left(n\right)=O\left(g\left(n\right)\right)
$$

If there are positive constants $c$ and $n_{0}$ such that:
$$
f\left(n\right)\le cg\left(n\right) \text{for } n\ge n_{0}
$$

If $f\left(n\right)$ is monotone (strictly increasing), at some point $n_{0}$, $G\left(n\right)$ will be always greater than $f\left(n\right)$. The constant must also never be greater than $n_{0}$

###### Example: 

$$
n=O\left(n^{2}\right)
$$

## Data structures

### Stacks

- A statck is just some objects on top of some other objects
- Example of the runtime stack

- The stack arbitrary ADT (abstract data type) stores arbitrary objects.
    - Insertions and deletions follow the **last-in first-out** scheme
        - The last object put on the stack will be the first to be taken out
    - Main stack operations:
        ```
            void push(object); // inserts an element
            object pop(void); // removes and returns the last inserted element
        ```
    - Auxiliary stack operations:
        ```
            object top(void); // returns the top element without removal
            int len(void); // returns the length of the stack; number of objects in the stack
            bool is_empty(); // returns whether the stack itself is empty
        ```
    - Example Application of stacks
        - Page-visited history in web browser
        - undo sequence in text editor
        - chain of method calls in code recursion

#### Array based stack implementation

We add elements from the left to right
- example:
```
    typedef struct {
        void *stack_items;
        int stack_pointer; // Stores the current where the top element is for push/pop operations
    } stack;
```
- return -1 for if empty. As the stack cursor can never reach -1 index, we know this handles our error.

#### Performance limitations

- Let $n$ be the number of elements in the stack
    - The space used is given by: $O\left(n\right)$
    - Each operation runs in time $O\left(1\right)$


#### Parentheses Matching
- Each open bracket type, ```('(', '{', '[', '|')``` There must be a closed bracket
- This problem can be solved by implementing a stack to keep track of the current open scope

Example with html:
```
def is_matched_html(raw):
    # Return true if all HTML tags are properly matched, or return false
    S=ArrayStack()
    j=raw.find('<')
    while j!=-1:
        k=raw.find('>',j+1)
        if k==-1:
            return False
        tag=raw[j+1:k]
        if not tag.startswitch('/'):
            S.push(tag)
        else:
        if S.is_empty():
            return False
        if tag[1:]!=S.pop()
            return False
        j=raw.find('<',k+1)
    return S.is_empty()
```

