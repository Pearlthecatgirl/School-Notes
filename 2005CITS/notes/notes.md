# Notes:

## Week 2 (Lectures 2):
For each:
has syntax 
```
for (Type element : collection)
    statement
```

The collection is the collection/list to be iterated over, type element is the type of the iterator and element is the name of the iterator

example: 
```
for (int i : my_int_array) statement
```

## Week 3 (Lecture 4):

### Scope

- Variables declared in **main** method will stay for the entire span of the program.
- Variables declared in other scopes will be discarded as soon as the scope has finished
- You can have an empty scope by itself:

```
public class Scopes {
    public static void main(String[] args) {
        if (true) {
            // Regular if scope
        }
        {
            // This is an empty scope
            // Variables declared here will be lost
        }
    }
}
```

### Typecasting and conversion

- int can convert into double without loss of information, but long cannot convert to int as long is more precise
    - Important to only convert from less precise to more precise



