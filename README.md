# CVM Financial Data Analysis

## About the Project
This repository contains an exploratory data analysis (EDA) script focused on the financial performance of public companies registered with the Brazilian Securities and Exchange Commission (CVM). The objective is to analyze the annual percentage variation in corporate revenues and profits across different economic sectors.

## Dataset
The data is publicly provided by CVM (Comissão de Valores Mobiliários). 
* **CVM Result.csv**: Contains the financial results (Revenue and Profit/Loss).
* **CVM registration data.csv**: Contains the corporate registration details, including the economic sector of each company.

*Note: Ensure these datasets are placed inside the `data/` directory as shown in the project structure below.*

## Tech Stack
* Python
* Pandas & NumPy (Data manipulation and cleaning)
* Seaborn & Matplotlib (Data visualization)

## Features
* **Data Cleaning:** Filtering specific accounting codes, handling missing values, and removing report duplicates.
* **Feature Engineering:** Calculating percentage variation year-over-year using lagged values.
* **Outlier Handling:** Removing statistically extreme variations (>-200% or <200%) to avoid skewed sectoral means.
* **Data Visualization:** Bar charts plotting the average revenue and profit variation by economic sector.

## Project Structure
```text
CVM - Project/
├── data/
│   ├── CVM registration data.csv
│   └── CVM Result.csv
├── src/
│   └── Script CVM.py
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## How to Run (using Makefile)

This project includes a `Makefile` to automate the environment setup, script execution, and cleanup processes. Make sure you have `python3` and `make` installed on your system.

### 1. Setup Environment
To create a virtual environment (`venv`) and install all required dependencies (from `requirements.txt`), run the following command in your terminal:
```bash
make setup
```

### 2. Run the Analysis
To execute the data analysis script using the virtual environment, run:
```bash
make run
```
*This will process the data and generate the final visualizations.*

### 3. Clean Project
If you want to remove the virtual environment and all generated cache files (`__pycache__`), run:
```bash
make clean
```