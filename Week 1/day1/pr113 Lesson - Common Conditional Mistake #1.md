## 🧠 Lesson: Common Conditional Mistake #1  
### ❌ **Using `or` instead of `and` for range checks**

### 🔎 The Mistake:
```python
age = 15
if age >= 13 or age <= 17:
    print("Teenager")
```

👎 Problem: This always prints `"Teenager"` — because even if `age = 30`, `30 >= 13` is `True`, and Python stops checking due to `or`.

---

### ✅ The Right Way:

```python
age = 15
if 13 <= age <= 17:
    print("Teenager")
```

✅ Cleaner and accurate — this will only be `True` for ages 13 to 17.

---

### 📝 Mini Exercise 1:

> ✏️ **Write a code snippet that checks if a number is between 100 and 200.**  
If it is, print `"In range"`, otherwise print `"Out of range"`.

Use input validation, then `if/else`.