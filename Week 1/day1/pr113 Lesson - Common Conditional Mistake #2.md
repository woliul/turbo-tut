### 🎯 Lesson: Common Conditional **Mistake #2**

## ❌ Mistake #2: Forgetting to Handle `Edge Cases` Properly

### 🔎 Example Mistake:
```python
age = 0
if age >= 1 and age <= 12:
    print("You're a child.")
```

👎 This code **skips age = 0** — but maybe you wanted to say "You're a baby!" or "Unborn or just born".

---

### ✅ Best Practice:
Handle edge cases early — either by:
- Adding a condition at the top:
  ```python
  if age < 1:
      print("You're a baby!")
  ```
- Or validating input and rejecting invalid numbers before branching:
  ```python
  if age < 0 or age > 120:
      print("Invalid age.")
      exit()
  ```

---

### 📝 Mini Exercise 2:

> ✏️ **Ask the user for a temperature in Celsius.**  
Then:
- If less than 0 → `"Freezing cold!"`
- 0–20 → `"Cold"`
- 21–30 → `"Warm"`
- Above 30 → `"Hot!"`
- If temperature is below **absolute zero (-273.15°C)**, show error and exit

Use input validation, and follow best practices from the previous lessons.

---

Ready when you are!