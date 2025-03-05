
## Week 2 (Lecture 1)

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

#### Sorting

