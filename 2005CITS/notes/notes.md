# Notes:

## Week 2 (Lectures 2):
For each:
has syntax 
```
for (Type element : collection)
    statement
```

The collection is the collection/list to be iterated over, type element is the type of the iterator and element is the name of the iterator

Example: 
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

- Manual casting follows c syntax

```
float x=5.5;
int y= (int)x;
\\ y=5
```

- Long (64 bits) will lose the top 32 bits and only keep the lower 32 bits.

```
10100010 00001000 10100011 11110010 -> 10100011 11110010
```

#### Type promotion

- char, byte, short promoted to int
- int promoted to long
- any integer promoted to float
- float to double

#### Control Statements

- if
    - runs only if condition is true, otherwise jumps past its scope
- else
    - similar to if
- if/else/if stack
    - chains if statements
- nested ifs
    - ifs within ifs
- switch statement
    - c style syntax:
    ```
    switch (expr) {
        case 1:
            break;
        case 2:
            break;
        default:
            break;
    }
    ```
    - case valeues must be constant
        - similar to c, it is building a lookup table
        - can be:byte, short, int, char, enum, string
- while
- break
    - jumps to the end of whatever loop
        - while, for, switch
- do while
- empty statements
    - just a semicolon ';'
    ```
        for (;;;) ;
        // For .... ever?
    ``` 
- arrays
    - type followed by []
    ```
        int[] // int array
        String[] // string array
    ```
- continue
    - similar to break
        - ends only the current iteration of the loop
        - skips to the next loop
- label:
    - similar to goto, but for break and continue
    ```
    out_of_for:
    for (int i=0;i<10;i++) {
        if (i>6) break out_of_for;
    }
    ```

#### classes
- contains fields and methods:
    - methods are like a function
    - fields are data
- example:
    ```
    class BankAccount {
        String ownerName;
        int balance;
    }
    ```

- A class is a *specification*
    - the above example does not mean a bank account has been opened yet, simply that if one were to open, it would follow that format
- to create an instance:
    ```
    BankAccount account=new BankAccount();
    ```
    - Note that account actually doesnt contain an instance of 'BankAccount', rather a reference
        - The 'BankAccount' object itself for 'account' is stored elsewhere in the heap, with its reference being in account
            - think of it as a pointer
            ```
            // Make a new account and make it the same object
            BankAccount account2=account;
            // Affecting account2 values will affect account1 values
            ```
- Access elements with a dot, as if it were a struct
    ```
    account.balance=3;
    ```
