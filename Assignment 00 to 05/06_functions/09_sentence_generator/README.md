# **📝 Sentence Generator 📖**  

#### **📌 Overview**  
This program takes a **word** from the user and categorizes it as a **noun, verb, or adjective**, then generates a sentence accordingly.

---

### **🛠 How It Works?**  

✅ **`make_sentence(word, part_of_speech)`**  
- Takes a **word** and its **part of speech** (0 = noun, 1 = verb, 2 = adjective).  
- Prints a sentence based on the **category**.  
- If an invalid number is entered, it **shows an error message**.

✅ **`main()`**  
1. Asks the **user for a word**.  
2. Prompts them to enter **0, 1, or 2** to classify the word.  
3. Calls `make_sentence()` to **generate the sentence**.

---

### **🔍 Example Run**  
#### **🖥 Input:**  
```
Please type a noun, verb, or adjective: rainbow
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 0
```
#### **✅ Output:**  
```
I am excited to add this rainbow to my vast collection of them!
```

---

### **🔄 Edge Case Handling**
- **If the user enters an invalid number (e.g., 3, -1, etc.),** the program prints:  
  ```
  Part of speech must be 0, 1, or 2! Can't make a sentence.
  ```

🎯 **Try it and create fun sentences!** 🚀