The Observer Pattern is a well-known object-oriented programming design pattern that represents the pub/sub relationship. But many developers, short of taking the right CS classes, never encounter functional programming alternatives. It's even more interesting to see how these can be done in #python.

This example shows how you can use closures to encapsulate the list of subscribers (observers/subjects). What you mean not know is that you can return many functions that have access to the closure's function scope. Here I demonstrate how we can use these functions to register and unregister subscribers and notify subscribers of new data. 

The clients here are pretty basic and each prints their data for visibility. Not shown in this example are the client functions--also closures, but could be proper class objects. See the codebase for the complete solution. One client shows the sum of values observed, another the last 3 (e.g., for reporting a rolling average), and the last just reports the most recent value. Clients like these could be used for building different reporting frontends of the same time series (e.g., weather data). From a design perspective, we could even use these observable funtions and use dependency injection to add them to our clients so the client can control when it registers/unregisters, since in the end its just passing functions into objects or other functions. Neat, yeah?

What tweaks have you done with the Observer Pattern? Have you used closures to implement other classic OOP design patterns? What changes would you make to this approach?

<img src="../../static/0012.png" />
