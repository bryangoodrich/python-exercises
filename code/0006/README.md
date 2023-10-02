Many developers learn about OOP principals of encapsulation, but in functional programming, the equivalent is implemented via closures. A closure stores function scope variables that state are accessible to nested functions within. One use case of this in #python is to create a similar behavior to useState
in JavaScript (React). You deconstruct (unpack) a state variable and update function from useState(...) and then update the state variable with that setter function.

To implement this in python, we can use closures. Here I demonstrate we can initialize a variable scoped to use_state but accessible (nonlocal) by the set_state nested function. This function is made available when we unpack the return tuple of state, set_state. Unlike proper FP languages, we have to use a complex type (dict here) to keep the object reference, because if we had used a vanilla int, the count variable would only ever reference the original state variable, not its updated versions. The benefit of something like this? We can create increment/decrement functions to encapsulate that counter behavior and use them accordingly, separating the state change from the use of the state variable in our applications. 

Have you used closures before? In production? What other functional programming concepts would you like to see? 

<img src="../../static/0006.png" />
