# Task 5: OOPs Architecture: Enterprise Smart Inventory & Asset System

## Overview
A production-grade inventory and asset management system written in Python 3 demonstrating strict **Object-Oriented Programming (OOP)** principles: Abstraction, Encapsulation, Inheritance, Polymorphism, and Python Dunder / Magic Methods.

---

## 🏛️ OOP Architecture & Design

### 1. Abstraction (`abc.ABC`, `@abstractmethod`)
- Abstract base class `Item` enforces implementation of:
  - `calculate_late_fee(days_overdue: int) -> float`
  - `get_item_type() -> str`

### 2. Encapsulation (`@property`, `@setter`)
- Private attributes (`__item_id`, `__title`, `__price`, `__is_checked_out`, `__borrower`) safeguard state.
- Setter properties enforce validation (non-empty strings, positive price values).

### 3. Inheritance & Polymorphism
- Derived classes:
  - `Book(Item)`: tracks `author` and `pages`. Late fee: $1.00 / overdue day.
  - `Magazine(Item)`: tracks `issue_number` and `publisher`. Late fee: $0.50 / overdue day.
  - `DigitalMedia(Item)`: tracks `format_type` and `file_size_mb`. Late fee: $2.00 / overdue day.

### 4. Dunder (Magic) Methods
- `__str__`: Informative readable representation for users.
- `__repr__`: Unambiguous developer debugging representation.
- `__len__`: Polymorphic length metric (pages for Book, issue number for Magazine, MB for Digital Media).
- `__eq__`: Value equality comparison based on unique `item_id`.

---

## 📁 Project Structure
```text
Task5_SmartInventory_OOP/
├── models.py       # Abstract Item base class and derived subclasses
├── inventory.py    # InventoryManager & interactive CLI
└── README.md       # Documentation
```

---

## 🚀 How to Run
```bash
python inventory.py
```
