# Student Record Management System

A beginner-friendly Python CLI application designed for simple file-based record keeping. It allows users to add student names along with their marks into a persistent text file, handles basic name duplicate checks, and displays the saved records in an indexed list.

---

## 📌 Project Overview

Managing basic records without an external database is an essential programming concept. This project demonstrates raw Python file handling concepts (`open`, `write`, `read`, `seek`, and `readline`) by maintaining student scores in a local file.

---

## ✨ Features

- **Duplicate Name Alert:** Checks the text file to notify if a student name already exists before appending.
- **Persistent Storage:** Uses standard text file I/O (`stored_names`) so records persist across program runs.
- **Interactive Data Entry:** Continuous loop to add multiple student records in a single session.
- **Formatted Display:** Reads line-by-line and prints all stored entries numbered sequentially.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts Used:** File Handling (`a+` and `r` modes), File Pointer Manipulation (`seek`), Loops, and String formatting

---

## 📂 File Output Format

Records are stored in plain text inside `stored_names` formatted as:

```text
Rahul Sharma : 85
Priya Verma : 92
Amit Patel : 78
