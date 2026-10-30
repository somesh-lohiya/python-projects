# CSV Data Quality Auditor

A lightweight Python command-line utility built to audit raw tabular datasets before ingestion or analysis. It scans CSV files to identify primary key duplicates and locate missing values across records.

---

## 📌 Problem Statement

Real-world datasets frequently contain dirty records—unintended duplicate entries or blank fields—which skew exploratory analysis, bias metrics, and break database constraints. This script provides a quick, zero-dependency validation check to spot data integrity issues early in the pipeline.

---

## ✨ Features

- **Primary Key Duplicate Detection:** Tracks frequencies of `Customer_ID` and flags duplicate occurrences along with count.
- **Null / Empty Value Detection:** Scans every column field to catch `None`, empty strings, or whitespace-only inputs, mapping missing fields directly to the corresponding `Customer_ID`.
- **Interactive CLI:** Simple menu allowing users to run duplicate checks, null checks, or both concurrently.
- **Zero External Dependencies:** Built entirely with Python's built-in `csv` module—no need to install heavy external packages.
