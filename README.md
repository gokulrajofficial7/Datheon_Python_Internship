# Datheon Python Programming Internship

Production-ready Python solutions for the **Datheon Python Programming Internship (1 Month / 4 Weeks)**.

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Tasks Completed](https://img.shields.io/badge/Tasks%20Completed-5%20of%205%20(100%25)-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📋 Comprehensive Task Pack (All 5 Tasks Completed)

| Directory | Task Title | Difficulty | Key Concepts Demonstrated |
| :--- | :--- | :--- | :--- |
| [`Task1_HangmanGame/`](./Task1_HangmanGame/) | **Hangman Word Guessing Game** | Beginner | Modular Game Architecture, Visual ASCII Gallows Stages, String Masking, Set-based Duplicate Penalty Prevention. |
| [`Task2_StockPortfolioTracker/`](./Task2_StockPortfolioTracker/) | **Stock Portfolio Tracker** | Beginner | Financial Calculations (P/L, Return %), Weighted Average Cost Basis, Market Feeds Ingestion, CSV Persistence. |
| [`Task3_FileOrganizer/`](./Task3_FileOrganizer/) | **Automated File Organizer** | Intermediate | Desktop Automation, `os`/`shutil`/`pathlib`, Collision Avoidance Suffixing, Structured Error Handling, Execution Audits. |
| [`Task4_ChatbotAssistant/`](./Task4_ChatbotAssistant/) | **Rule-Based Assistant Chatbot** | Beginner | Multi-Intent Classification, Regular Expressions (`re`), JSON Knowledge Base (`sample_faq.json`), Fallback Scoring. |
| [`Task5_SmartInventory_OOP/`](./Task5_SmartInventory_OOP/) | **Enterprise Asset System (OOP)** | Intermediate | Strict OOP Architecture, Abstract Base Classes (`abc.ABC`), Encapsulation (`@property`), Polymorphism, Dunder Methods. |

---

## 🏛️ Architecture & System Highlights

1. **Task 1: Hangman Word Guessing Game**
   - 7-stage progressive ASCII gallows visualization.
   - Set-based tracking of guessed characters preventing repeated penalty deductions.
   - Ingests from external `words.txt` with robust fallback arrays.

2. **Task 2: Stock Portfolio Performance Tracker**
   - Real-time valuation calculations (Invested Capital, Current Market Value, Gain/Loss, Percentage Returns).
   - Ingests market quotes from `constituents.csv` and auto-persists transaction summaries to `portfolio_summary.csv`.

3. **Task 3: Automated File Organizer & Cleanup Utility**
   - Autonomous directory restructuring across 30+ extension mappings into categorized subfolders (`/Documents`, `/Images`, `/Videos`, `/Audio`, `/Archives`, `/Code`, `/Others`).
   - Intelligent collision handling renaming identical files sequentially (`file_1.pdf`).
   - Built-in safe mock directory generator for instant demo testing.

4. **Task 4: Rule-Based Interactive Terminal Assistant / Chatbot**
   - Pattern matching engine using regular expression word boundaries and scoring.
   - Dynamic JSON FAQ knowledge base ingestion.
   - Conversational state management with contextual fallbacks.

5. **Task 5: Enterprise Smart Inventory & Asset System (OOP)**
   - Strict abstraction via Python `abc.ABC` and `@abstractmethod`.
   - Private attribute encapsulation (`__item_id`, `__price`) guarded by `@property` and `@setter` validation.
   - Polymorphic inheritance hierarchy (`Book`, `Magazine`, `DigitalMedia`) with domain-specific late fee algorithms.
   - Custom dunder methods (`__str__`, `__repr__`, `__len__`, `__eq__`) for clean Pythonic manipulation.

---

## 🚀 Quick Start & Execution

```bash
# Task 1: Hangman Console Game
cd Task1_HangmanGame && python hangman.py

# Task 2: Stock Portfolio Tracker
cd Task2_StockPortfolioTracker && python portfolio.py

# Task 3: Automated File Organizer
cd Task3_FileOrganizer && python organizer.py

# Task 4: Interactive Rule-Based Chatbot
cd Task4_ChatbotAssistant && python chatbot.py

# Task 5: Enterprise Smart Inventory (OOP)
cd Task5_SmartInventory_OOP && python inventory.py
```

---

## 👨‍💻 Verification & Submission
- **Developer:** Gokulraj A R
- **GitHub Repository:** [gokulrajofficial7/Datheon_Python_Internship](https://github.com/gokulrajofficial7/Datheon_Python_Internship)
- **Internship Organization:** [Datheon](https://www.datheon.in/)
- **Track:** Python Programming Internship (Python & AI Applications)
