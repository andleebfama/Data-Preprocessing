# Titanic Data Preprocessing

## Project Overview
This project involves cleaning and preprocessing the famous Titanic dataset to prepare it for further analysis or machine learning tasks. The dataset contains information about passengers, and the goal is to handle missing values, convert categorical data to numerical format, and normalize numeric features.

## About the Project
- Dataset used: Titanic - Machine Learning from Disaster (Kaggle)
- Tools & Technologies: Python, Pandas, scikit-learn
- Main steps performed:
  - Dropped columns with excessive missing values
  - Filled missing values with mean or mode
  - Encoded categorical variables (`Sex` and `Embarked`) into numeric values
  - Normalized numerical columns (`Age`, `Fare`, `SibSp`, `Parch`)
  - Saved the cleaned dataset for future use

## How to Use
1. Clone or download this repository.
2. Make sure Python and required libraries (`pandas`, `scikit-learn`) are installed.
3. Run the preprocessing script:
   ```bash
   python data_preprocessing.py
