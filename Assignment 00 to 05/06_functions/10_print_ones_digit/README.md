# **🔢 Print Ones Digit Program**  

#### **📌 Overview**  
This program extracts and prints the **ones digit** (last digit) of any integer, including **negative numbers**.

---

### **🛠 How It Works?**  

✅ **`print_ones_digit(num: int)`**  
- Extracts the **ones digit** using `abs(num) % 10`.  
- The `abs()` function ensures it works for **negative numbers** too.  
- Prints the **ones digit**.

✅ **`main()`**  
1. Asks the user to **enter a number**.  
2. **Handles invalid inputs** (ensures the input is an integer).  
3. Calls `print_ones_digit()` to **display the result**.

---

### **🔍 Example Runs**  

#### **🖥 Input 1:**  
```
Enter a number: 1234
```
#### **✅ Output:**  
```
The ones digit is 4
```

---

#### **🖥 Input 2:**  
```
Enter a number: -567
```
#### **✅ Output:**  
```
The ones digit is 7
```

---

### **🔄 Edge Case Handling**
- **If the user enters invalid input (e.g., "abc", "12.5")**, the program prompts:  
  ```
  Invalid input. Please enter a valid integer.
  ```
- Works correctly for **negative numbers** due to `abs(num)`.

🎯 **Try it out with different numbers!** 🚀