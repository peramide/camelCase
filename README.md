# 🐍 Camel to Snake Case Converter

A simple Python program that converts variable names from **camelCase** to **snake_case**. It helps demonstrate string manipulation, loops, and Python’s naming conventions.

---

## 📄 Description

In `camel.py`, the program prompts the user for a variable name written in **camel case** (e.g., `thisIsCamelCase`) and outputs the equivalent **snake case** form (e.g., `this_is_camel_case`).

Camel case is common in languages like JavaScript and Java, while Python follows snake case for variable names.

---

## ⚙️ How It Works

1. The user enters a camelCase variable name.
2. The program iterates through each character.
3. Whenever an uppercase letter is found, it adds an underscore `_` followed by the lowercase version of that letter.
4. The final output is displayed in snake_case.

---

## 🧪 How to Test

Run the program in your terminal:

```bash
python camel.py
```

Then, test with the following examples:

| Input                | Expected Output        |
| -------------------- | ---------------------- |
| `name`               | `name`                 |
| `firstName`          | `first_name`           |
| `preferredFirstName` | `preferred_first_name` |

---

## 💡 Example

```bash
$ python camel.py
camelCase: preferredFirstName
snake_case: preferred_first_name
```

