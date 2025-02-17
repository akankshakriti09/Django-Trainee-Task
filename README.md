##django_signals

**Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer: By default, Django signals are executed synchronously. This means that when a signal is sent, all the connected receiver functions are executed immediately in the same thread before the execution continues.

* When a sender dispatches a signal, all registered receivers are called one by one in the order they were connected. 
* If a receiver function takes time to execute (e.g., making an API call, processing a large file), it will block the main thread until it completes.


Code Conclusion: Proving Signals are Synchronous
1. The "Total execution time" includes the 3-second delay from the signal.
2. If the signal was asynchronous, the execution time would be close to 0 seconds, because the request would continue without waiting for the signal.
3. Since the request waits for the signal to complete, it proves Django signals run synchronously by default.

By default, Django signals execute synchronously, meaning:
1. They block further execution until the signal handler finishes.
2. They can slow down request processing if they include expensive operations.