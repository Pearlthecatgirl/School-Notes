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


##### Enums

Syntax: 
```
enum MyEnum {
    VALUE1, VALUE2, VALUE3, VALUE4
}
// Convention to use capitals

// Usage:
MyEnum thisvariable = MyEnum.VALUE1;
```
- can be compared with '=' because int under the hood
- can use as if it were an int in switch
- enums are classes, so they can be public, protected, private or default like any class
    - however, there is no inheritence (no extend)
    - they do have their own methods
    - you can add your own methods

<code>

enum Transport {
    // the value of each enum "member" can be set too
    BUS(50), TRAIN(100), FERRY(20), TRAM(30),

    // similar to class, there can be "const" members in enums
    private final int typicalSpeed;

    // A constructor, (notice the same name?) 
    // It sets the typicalspeed of the value...
    // calling Transport.TRAIN will probably call the constructor..?
    Transport(int typicalSpeed) {
        this.typicalSpeed=typicalSpeed;
    }

    // just some getter method
    public int getTypicalSpeed() {
        return typicalSpeed;
    }
}

public class EnumConstructor {
    public static void main(String[] argv) {
            System.out.println(Transport.BUS.getTypicalSpeed());
    }
}
</code>

##### Autoboxing and unboxing

- Autoboxing: automatically convert from primitive to object type
- Unboxing: automatic conersion from object to primitive
- "place the primitive type in a box, which is the object we have"

##### Generic Types

##### OOP Principles

- Principles about writing clean OOP code (SOLID principle)
    - SOLID:
        - Single-responsibility principle
            - A class should have only 1 reason to change:
            - Single reason means single responsibility
            - A class should not be responsible for too many things (imagine like... KISS principle)
            - class should do 1 thing, 
            - only 1 source of specification can modify our class.
                - having multiple specifications that can effect our class mean there is more responsibility
                - <code>
                    public class mazeSolver {
                        public void setwallposition() {} 
                        // This should not be in this class. 
                        // a "solver" class should not need to modify the maze
                        public Path findPath() {}
                } </code>
                - instead split into having a solver class and a modify maze class
        - Open–closed principle
            - software should be open for extension but closed for modification
            - Open for extension: we can add new functionality (don't make a final class...?)
            - closed for modification: idealy we should not change the existing code to add new functionality
                - see above for single response principle
            - add new features by making new classes/methods, not by modifying existing code
            - encourages interface and abstract usage.
        - Liskov substitution principle
            - subtypes should be subsitutable for their base types without affecting the correctness of the program
            - a subclass should be able to pretend to be its superclass without breaking anything
            - anthing true for a square should be true for a shape -> as a square is a shape
                - square can pretend to be a generic shape and have all conditions to shape apply to square
            - new derived class should not introduce unexpected behaviour:
                <code>
                    class bird {void fly() {}}
                    class penguin extends bird {
                    @Override
                    void fly() {}
                    }
                </code>
            - penguin cannot subsitute a generic bird, because penguins can't fly
        - Interface segregation principle
            - Clients should not be forced to depend on methods they do not use
            - lots of smaller interfaces are usually better than one big class/interface
            - make an interface for each different method
            - enhances maintainability and readability
            - interfaces can be fused anyway
        - Dependency inversion principle
            - High level models should not depend on low-level models; both should depend on abstractions
            - Abstractions should not depend on details, details should depend on abstractions
            - don't store classes, store interfaces


#### Concurrency and multithreading:

- Usually processes run on single threads
- If there is only 1 core, computer will schedule the processes
- Two processes running at the same time is called **Concurrency**
    - Processes never run at the same time, just they are scheduled so they run as if they are running side by side
- Example usage:
- A gui file editor:
    - load the gui while loading the file
    - use 1 thread to read file
    - use another thread to load the gui
 
Thread vs process:
- Threads have access to shared memory (as they are the same program)
- Processes are described as different programs

Java supports by default multithreaded code
- Each instance represents a new thread of execution

Thread usage example:

```
class myThread extends Thread {
    private int num;
    public myThread(int num) {this.num=num}
    @Override 
    public void run() {
        System.out.print(num);
    }
}

public class ThreadExample {
    public static void main(String[] argv) {
        for (int i=0;i<10;i++) {
            myThread x=new myThread(i);
            x.run();
        }
    }
}
```

- The run() function is run concurrently.
- Not necessarily run in 1,2,3,4,5,6... order

Waiting:
- call the "join()" method from the main thread to wait for a sub-thread to finish:
- The sub-thread will join when its code has finished executing

```
class myThread extends Thread {
    private int num;
    public myThread(int num) {this.num=num}
    @Override 
    public void run() {
        System.out.print(num);
    }
}

public class ThreadExample {
    public static void main(String[] argv) {
        Thread[] threads=new Thread[10];
        for (int i=0;i<10;i++) {
            threads[i]=new myThread(i);
            x.run();
        }
        for (int i=0;i<10;i++) {
            try {
                threads[i].join();
            } catch (InterruptedException IE) {}
        }
    }
}
```

##### Race Condiiton:

- When two threads try to do an operation at the same time and the order of execution changes the result.
- Example:
- Good: A reads 0, A writes 1, B reads 1, B writes 2
- Bad: A reads 0, B reads 0, A writes 1, B writes 1
- To fix this, we can try: autobox primitive values so that they are no longer mutable. 

Fix For race condition: "Synchronized" statements

```
synchronized (object) {

}
```

- works with all objects

- When the thread enters the block above, the thread will try to lock (think creating a mutex). If the block is already locked, then it will wait until it is available.
- Nothing within the block can have a race condition, but which block runs first is still not determined. 

- A whole method can be described to be synchronized:

```
public synchronized mymethod() {}
```
##### Deadlock

- Two threads and two objects
- the first thread gets a lock on the first object while the 2nd thread gets a lock on the 2nd object
- they both need both objects to execute
- they both wait for the other to finish
- They will wait forever.

##### Interthread communication
- threads talk to each other

```
wait();
```

- Used to put the current thread into a "waiting" state
- must be called from a synchronized context
- the thread releases the lock on some object and waits until another thread calls ```notify()``` to signify something has been done.
    - notify() calls 1 thread (wakes up 1 thread?)
    - notifyAll() calls all threads.


















