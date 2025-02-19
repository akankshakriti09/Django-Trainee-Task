
## django_signals - Project Folder for Question 1 

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

## signal_test - Project Folder for Question 2

**Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer : Yes, Django signals run in the same thread as the caller by default. This means that if a signal handler is connected to a particular signal and that signal is sent, the handler executes synchronously in the same thread as the sender.

Implications:
1. Blocking Execution: Since signals run synchronously, if a signal handler performs a time-consuming task (e.g., making API calls, sending emails, or performing database queries), it can slow down the main request/response cycle.
2. Error Handling: If an exception occurs in a signal handler and is not caught, it may affect the caller's execution.

Code Conclusion: Proving Django signals run in the same thread as the caller
1. The output shown that all threads IDs matched.
2. Since all thread IDs match, this confirms that Django signals run in the same thread as the caller.

##  - Project Folder for Question 3