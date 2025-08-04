# Python Recursion:

Welcome to this fun and beginner-friendly guide on **Python Recursion**!  
Whether you’re new to coding or just trying to crack the recursion puzzle — this post (with code + comic sketch) will walk you through:

---

## 📚 What You'll Learn

✅ What is Recursion  
✅ Base Case and Recursive Case  
✅ Stack Overflow in Recursion  
✅ Memoization & Why It's Powerful  
✅ Python's `@lru_cache` Decorator  
✅ Real example: Fibonacci using Memoization

---

## 🧠 What is Recursion?

> A function calling itself to solve smaller chunks of a problem.

```python
def say_hello(n):
    if n == 0:
        print("Stop")
    print("Hello")
    say_hello(n-1)
```

What is Stack Overflow?⚠️ 

Recursion without a stop (base case) leads to memory overload.

```python
def call_me():
    return call_me()
```

call_me()  #  Will crash: RecursionError: maximum recursion depth exceeded


Memoization to the Rescue🚀 

Memoization stores results of expensive function calls and returns cached result when the same inputs occur again.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55
```
📌 @lru_cache helps us avoid recalculating the same results.

🧵 Want to Learn More?

Check out:
	•	Official Python Docs – [functools](https://docs.python.org/3/library/functools.html)
	•	Instagram  & Youtube : @learnwithbhawana
 
Test It Yourself

You can try:
	•	Countdown with recursion
	•	Factorial calculation
	•	Fibonacci with and without memoization



 💬 Have Questions?
Drop your doubts in the comments or DM on Insta @learnwithbhawana. Let’s grow together! 🌱

⸻

📌 Keywords
python, recursion, memoization, lru_cache, beginner python, fibonacci, stack overflow, coding fun, coding 
