# Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

## Overview
A responsive, rule-based conversational terminal assistant built with Python 3. It utilizes regular expressions, keyword tokenization, and multi-intent matching to answer user questions loaded dynamically from a JSON knowledge base (`sample_faq.json`).

---

## 🛠️ Key Features
- **JSON Knowledge Base:** Ingests patterns and responses from `sample_faq.json` for easy extensibility.
- **Multi-Intent Recognition:** Uses regular expressions (`\b` word boundaries) and phrase length scoring to classify queries into appropriate intent buckets (Greetings, Hours, Services, Pricing, Internship, Contact, Goodbye).
- **Graceful Fallback Handling:** Employs fallback responses with suggestions when user confidence falls below threshold.
- **Conversational State Loop:** Clean input normalization and conversational session loop with exit commands (`exit`, `quit`, `bye`).

---

## 🚀 How to Run
```bash
python chatbot.py
```
