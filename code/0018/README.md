Monads are a design pattern used in functional programming. They allow you to write functions in a more mathematically pure way, which enables building more stable and easily tested code. 

If you define a function that takes an int, and then have *if* all over to handle the case when an input is None in #python, you lied. Your function takes an int or a None. The Maybe or Option Monad allows you to write your functions without this constant checking because the Monad encapsulates that behavior. Your functions now take in a Maybe<int> and return either a None or int.

Have you heard of Monads before? Do you use any in production? Would you want to see how the Writer handles logging or Result Monad handles errors?

<img src="../../static/0018.png" />
