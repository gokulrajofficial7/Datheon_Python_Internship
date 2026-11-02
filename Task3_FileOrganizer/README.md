# Task 3: Automated File Organizer & Cleanup Utility

## Overview
An autonomous desktop automation utility that organizes cluttered directories (e.g., Downloads, Desktop, shared workspace folders) by inspecting file extensions and grouping them cleanly into categorized subdirectories (`/Documents`, `/Images`, `/Videos`, `/Audio`, `/Archives`, `/Code`, `/Others`).

---

## 🛠️ Key Features
- **Dynamic Extension Categorization:** Automatically maps 30+ common extensions into logical directory trees.
- **Collision Resolution:** Automatically avoids overwriting identically named files by adding indexed suffixes (`file_1.pdf`).
- **Error Resilient:** Implements structured `try...except` handling for `PermissionError` and file locks.
- **Summary Reporting:** Prints total files relocated, breakdown per category, and error metrics.
- **Self-Contained Demo Mode:** Allows testing safe reorganization on a generated mock directory without altering your personal files.

---

## 🚀 How to Run
```bash
python organizer.py
```
