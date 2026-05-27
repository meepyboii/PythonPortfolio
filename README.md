# PythonPortfolio
projects i created at jones college prep from 2025-2026

# Multi-Project Repository: Python Applications, Games & Utilities

Welcome to this collection of Python applications. This repository showcases a variety of programming concepts, including conditional narratives, modular arithmetic, data-driven lookup services, decision trees, and randomized simulation utilities.

---

## 📂 Repository Structure

* `adventure_game.py` — A choice-driven narrative escape game.
* `calculator.py` — A modular command-line basic calculator.
* `coffee_recommender.py` — An interactive menu assistant using nested decision paths.
* `sorting_hat.py` — A randomized Hogwarts house sorting simulator with built-in character easter eggs.
* `birds.py` — An interactive search utility that parses bird data from an external CSV file.
* `birds.csv` — The dataset containing bird names, scientific data, colors, diets, and image URLs.

---

## 🎮 1. Adventure (`adventure_game.py`)

### Description
A minimalist, text-based choice game. Players find themselves trapped in a mysterious secret room and must navigate their way to freedom by making a series of critical binary decisions.

### Features
* **Branching Storylines:** Every choice matters, leading players down entirely different narrative paths.
* **Multiple Endings:** Features 4 distinct outcomes, ranging from ultimate wealth and success to darkly comedic demises.

### How to Play
1. Run the script: `python adventure_game.py`
2. Follow the on-screen prompts to choose your path (e.g., `rat` vs `snake`, `left` vs `right`).

---

## 🧮 2. Basic Calculator (`calculator.py`)

### Description
A clean, functional command-line calculator that prompts the user for two integers and an arithmetic operator, executing the calculation through dedicated mathematical functions.

### Features
* **Modular Code Structure:** Uses separate, specialized functions for addition, subtraction, multiplication, and division to keep code highly organized.
* **Error Handling:** Gracefully handles invalid mathematical operators without crashing.

### How to Run
1. Run the script: `python calculator.py`
2. Enter your two integers and pick from the supported operators: `+`, `-`, `*`, `/`.

---

## ☕ 3. Le Cafe Recommender (`coffee_recommender.py`)

### Description
A simple, interactive menu assistant designed to recommend the perfect drink. The script mimics a basic customer service chatbot by filtering menu options based on user taste preferences.

### Features
* **Nested Logic:** Uses nested `if-elif-else` conditional branches to map out a clear decision-tree layout.
* **Tailored Outputs:** Analyzes temperature and sweetness combinations to recommend one of four distinct drink options.

### How to Run
1. Run the script: `python coffee_recommender.py`
2. Answer the questions about your temperature and sweetness preferences to get your drink recommendation.

---

## 🧙‍♂️ 4. Hogwarts Sorting Hat (`sorting_hat.py`)

### Description
An interactive simulation of the famous Harry Potter Sorting Hat ceremony. It prompts users for their name and assigns them to one of the four legendary Hogwarts houses.

### Features
* **Pacing & Suspense:** Integrates Python's built-in `time` library (`time.sleep()`) to generate realistic pause delays that mimic dramatic cinematic tension.
* **Easter Eggs:** Contains hardcoded conditional exceptions for iconic universe characters (e.g., inputting "Harry" guarantees Gryffindor, while "Voldemort" forces Slytherin).
* **Algorithmic Randomization:** Utilizes the `random` library to fairly distribute unrecognized names into a random house.

### How to Run
1. Run the script: `python sorting_hat.py`
2. Enter your name and wait for the sorting decision. Type `yes` to get sorted again, or `no` to exit.

---

## 🦅 5. Top Bird Lookup Service (`birds.py`)

### Description
Developed as a College Board AP CSP Create Task, this data-driven application helps users search, filter, and explore ecological information about various bird species using an external CSV dataset.

### Features
* **Multi-Criteria Search:** Search for birds by Common Name, Conservation Status, Primary Color, or Diet.
* **Browser Integration:** Looking up a bird automatically launches your default web browser to display a picture of the species.
* **Data Structures:** Leverages `pandas` and parallel list indexing to cross-reference data seamlessly.

### Prerequisites
This script requires the `pandas` library. You can install it via pip:
```bash
pip install pandas

