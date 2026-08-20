# CVM Financial Data Analysis

## About the Project
This repository contains an exploratory data analysis (EDA) script focused on the financial performance of public companies registered with the Brazilian Securities and Exchange Commission (CVM). The objective is to analyze the annual percentage variation in corporate revenues and profits across different economic sectors.

## Dataset
The data is publicly provided by CVM (Comissão de Valores Mobiliários). 
* **CVM Result.csv**: Contains the financial results (Revenue and Profit/Loss).
* **CVM registration data.csv**: Contains the corporate registration details, including the economic sector of each company.

## Tech Stack
* Python
* Pandas & NumPy (Data manipulation and cleaning)
* Seaborn & Matplotlib (Data visualization)

## Features
* **Data Cleaning:** Filtering specific accounting codes, handling missing values, and removing report duplicates.
* **Feature Engineering:** Calculating percentage variation year-over-year using lagged values.
* **Outlier Handling:** Removing statistically extreme variations (>-200% or <200%) to avoid skewed sectoral means.
* **Data Visualization:** Bar charts plotting the average revenue and profit variation by economic sector.