
## django_signals - Project Folder for Question 1 

**Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer: By default, Django signals are executed synchronously. This means that when a signal is sent, all the connected receiver functions are executed immediately in the same thread before the execution continues.

* When a sender dispatches a signal, all registered receivers are called one by one in the order they were connected. 
* If a receiver function takes time to execute (e.g., making an API call, processing a large file), it will block the main thread until it completes.


**Code Conclusion :** 
Proving Signals are Synchronous
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

**Code Conclusion :** 
Proving Django signals run in the same thread as the caller
1. The output shown that all threads IDs matched.
2. Since all thread IDs match, this confirms that Django signals run in the same thread as the caller.

## signals_demo - Project Folder for Question 3

**Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer : Yes, by default, Django signals run in the same database transaction as the caller. This means that if a signal handler performs database operations, those operations occur within the same transaction as the original model save, and they are subject to rollback if the transaction fails.

**Code Conclusion :** 
Proving Django signals run in the same database transaction as the caller
1. When an Author instance is created, the post-save signal triggers and attempts to create a Book instance.
2. If an exception occurs inside the transaction, both the Author and Book creations are rolled back.
3. The output confirms this by returning: Book exists after rollback: False


## custom_class_python - Project Folder for : 
## Topic: Custom Classes in Python

**Description: You are tasked with creating a Rectangle class with the following requirements:**
1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

**Code Conclusion :** 
When iterating over an instance of the Rectangle class, the output is:
{'length': 10}
{'width': 5}

This confirms that:
1. The iteration starts with the length in the format {'length': VALUE}.
2. The iteration follows with the width in the format {'width': VALUE}.
3. The order of output matches the requirements.

Thus, the implementation works correctly and meets all the specified conditions. 
