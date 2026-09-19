# CVM Financial Data Analysis

This repository contains an exploratory data analysis (EDA) script focused on the financial performance of public companies registered with the Brazilian Securities and Exchange Commission (CVM). The objective is to analyze the annual percentage variation in corporate revenues and profits across different economic sectors.

## Repository Structure

* `data/`: Directory containing the datasets (`CVM registration data.csv` and `CVM Result.csv`).
* `src/`: Directory containing the Python scripts.
  * `Script CVM.py`: Main script for data cleaning, merging, feature engineering, and visualization.
* `Makefile`: Automates the environment setup and data pipeline execution.
* `requirements.txt`: Lists Python dependencies required for the project.
* `.gitignore`: Specifies intentionally untracked files to ignore.

## Requirements

* Python 3.x
* pandas
* numpy
* seaborn
* matplotlib

## How to Run

**Note for Windows Users:** The Makefile commands are designed for Unix environments (Linux/macOS). If you are on Windows, please use Git Bash or WSL to run the pipeline.

**1. Clone the repository and access the folder**
```bash
git clone https://github.com/aldalisgomes/CVM-financial-analysis.git
cd CVM-financial-analysis
```

**2. Create and activate the virtual environment (Required on newer Debian/Ubuntu-based systems, such as WSL)**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies and run the pipeline**
```bash
make setup
make run
```

## Alternative for Windows (Or No Make Installed)

If you are using standard Git Bash, PowerShell, or Command Prompt without `make` installed, you can simply run the Python script directly after activating your virtual environment:

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the analysis script:**
*(Note: Use quotes around the script name because it contains a space)*
```bash
python "src/Script CVM.py"
```

## Data Pipeline Details

* **Data Import & Merging:** Reads CVM financial results and registration datasets with latin1 encoding and merges them by company code to include economic sectors.
* **Filtering:** Isolates specific accounting codes for Revenue (3.01) and Profit/Loss (3.11).
* **Cleaning:** Removes duplicate report versions and handles missing values to ensure data integrity.
* **Feature Engineering:** Calculates the year-over-year percentage variation using lagged financial values.
* **Outlier Handling:** Excludes statistically extreme variations (greater than 200% or less than -200%) to avoid skewed sectoral means.
* **Data Visualization:** Generates bar charts plotting the average revenue and profit variation by economic sector, filtering out sectors with insufficient observations to ensure statistical relevance.