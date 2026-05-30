# KDA and MVP Calculator

## Overview
This Python script is a simple and effective tool designed to calculate a player's KDA (Kills, Deaths, Assists) ratio and determine their MVP score based on standard MOBA / Battel Royal gaming metrics. It uses custom weightage for kills, assists, and death penalties to evaluate overall match performance.

## Features
* **KDA Calculation:** Safely computes the KDA ratio, handling the zero-death edge case by treating effective deaths as 1 to avoid division by zero errors.
* **MVP Score Evaluation:** Uses a custom weighted scoring system to accurately calculate the MVP score.
* **Robust Error Handling:** Implements `try-except` blocks (ValueError) to ensure the program does not crash upon receiving invalid or non-numeric user inputs.

## Scoring Logic
* **KDA Ratio Formula:** `(Kills + Assists) / Effective Deaths`
* **MVP Score Formula:** `(Kills * 5) + (Assists * 3) - (Deaths * 2)`

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Clone this repository and navigate to the project directory.
3. Run the script via your terminal:
   `python filename.py`
4. Enter your total kills, deaths, and assists when prompted.
5. The program will instantly output your exact KDA ratio and MVP score.