# 🐍 MLOPS_OOPS — Python OOPs Concepts with Examples

This repository is a **complete beginner-to-advanced guide** to learning Object-Oriented Programming (OOP) in Python, with practical scripts covering real-world concepts. Designed as part of an MLOps-themed learning series, this project walks you through all major OOP features including:

- Classes and Objects
- Inheritance (All Types)
- Encapsulation
- Static Methods
- Getters and Setters
- A Console-Based Project: `ChatBook`

---

## 📁 Repository Structure

MLOPS_OOPS/
├── OOPS1.PY # Basics: Class, Object, init(), simple methods
├── inheritance.py # Inheritance: Single, Multilevel, Hierarchical
├── typeof_inheritance.py # Complete inheritance types including hybrid
├── oops_proj.py # Covers encapsulation, static methods, setters/getters
├── random.py # Similar to oops_proj.py with variations
├── rough.py # Experimental or practice code
├── content.txt # Concept summary or explanations
├── LICENSE # MIT License
└── README.md # You're here!


---

## 🔑 Key Topics Covered

| Concept            | File(s)                | Description |
|-------------------|------------------------|-------------|
| **Class & Object**       | `OOPS1.PY`               | How to define classes, create objects |
| **Single Inheritance**   | `inheritance.py`         | Base → Derived structure |
| **Multilevel Inheritance** | `inheritance.py`       | A → B → C |
| **Hierarchical Inheritance** | `inheritance.py`     | A → B, A → C |
| **Multiple & Hybrid Inheritance** | `typeof_inheritance.py` | Demonstrates MRO, `super()` usage |
| **Encapsulation**       | `oops_proj.py`, `random.py`, `rough.py` | Private variables, getter/setter |
| **Static Methods**      | `oops_proj.py`           | Use of `@staticmethod` |
| **Mini Project - ChatBook** | `chatbook` class (in `oops_proj.py`) | Console-based login/posting system |

---

## 📦 `ChatBook` Project (Mini OOP Application)

A simple text-based interface to simulate a social media platform with features:

- Sign Up / Sign In
- Post content
- Send messages
- Use of private variables and static class variable (`user_id`)
- Console-based menu navigation

```python
class chatbook:
    __user_id = 1
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default user'
        ...
