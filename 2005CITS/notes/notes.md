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

#### String class

- Strings are immutable
    - cannot be changed
    - cannot dereference
        - for equality checking, use .equals()
            - most non primative objects should use this

#### Access modifiers

- Fields in a class can be declared as *private* or *public*    
    - private means this field can only be accessed within the class
        - This usually means using getters and setters to access information
        - Data hiding and **encapsulation**
    - public means any other class can access these fields
    - If 2 instances of 1 class have a private field, both instances can access that private field, allowing for copying. Example:

```
    public void copyInto(safearray other) {
        if (size<=other.size) for (int i=0;i<other.size;i++) other.array[i]=array[i];
    }
```    
Notice that other.array[] is private, but can still be accessed as they are both instances of the same class.

#### Overloading of methods

- Multiple methods in java can have the same name, as long as they are distinguishable (different parameters)
- This is essentially python's non-arguments 
- Note that the return type is **NOT** part of the signature, so it doesnt matter if they are the same or not, only the function name and arguments
- Constructors can be overloaded as well

#### Static Keyword

- a static method exists and functions on its own, and can be called without the need for a class.
- the main function can be called without calling the class, while a method within another class may need to be called upon its class.
- Fields can also be static, but they are 1 per class. Creating a new instance of that class will have the same 1 static field as the one before

#### Inheritance

- Code reuse and abstraction
- Make a subclass
    - Subclass inherits all members (fields and methods but not constructors)
    - Subclass can have move features on top of its inherited ones

##### Extends keyword

- copies all fields and methods that aren't private

has the following syntax: 

```
public class sub_class extends super_class {

}
```
Where super_class is the parent of this sub_class

##### Protected keyword

- protected is similar to private, but it can be accessed by subclasses.

##### Default access modifier

- When no access modifier is given

- In a class, when fields are not initialised they are automatically set to zero values
    - objects and arrays are set to null
    - Boolean are set to false

##### Method overriding and polymorphism

- dynamic dispatch
    - If i have a class variable being created using a subclass constructor, it will know at runtime to call the method in the constructor rather than the type. 
```
    class animal {
        public void talk() {
        }
    }
    class dog extends animal {
        public void talk() {
        }
    }
    animal newAnimal=new dog();
```
    This will use the dog version of talk rather than the animal version of talk.

- Methods can only override when the signature is exactly the same.

- @Override keyword
    - Notifies the compiler that this method should override a method from its superclass.



##### Packages

- Namespaces
    - allows 2 different things with the same name so long as they are in different namespaces
        - like multiple dirs
    - Encapsulates a collection of classes

- Usage (Definition):
```
    // Name_of_file
    package my_package;
```
Put the class in the a folder with the same name as the package.
```
/path/to/proj/my_package/Name_of_file.class
```

- Can have nested packages, all with respect to the root dir of the project, compile from the root dir

- Accessing
    - Usage:
    ```
        import my_package
    ```
    - Can import subpkgs
- JARs
    - Turn packages into a jar for distribution

- Packages and access modifiers

|Access Modifier| Class | Package| Subclass| world|
|-|-|-|-|-|
|Public|Y|Y|Y|Y|
|Protected|Y|Y|Y|N|
|Default|Y|Y|N|N|
|Private|Y|N|N|N|
