# 💳 Loan Risk Analysis & Feature Engineering

An end-to-end data analysis project exploring loan applications, data quality, borrower risk characteristics, and default behavior.

The project includes data cleaning, outlier treatment, feature engineering, risk segmentation, exploratory analysis, and an interactive Streamlit dashboard.

🌐 **Live Dashboard:**
https://loanriskanalysis-fsdruxvvfezgn4fa9ieffs.streamlit.app/

Live Demo: 
https://www.youtube.com/watch?v=uZDWw_EUwCs

💻 **GitHub Repository:**  
https://github.com/Uzma-Jawed/Loan_risk_analysis

---

## 📌 Project Overview

This project analyzes a dataset of **1,000 loan applications** to understand applicant characteristics and identify patterns associated with loan defaults.

The analysis focuses on:

- Data quality and missing values
- Invalid loan amounts
- Outlier treatment
- Feature engineering
- Credit-score-based risk segmentation
- Debt-to-income ratio
- Default-rate analysis
- Interactive visualization through Streamlit

The final result is an interactive web dashboard that allows users to explore the loan data and risk categories.

---

## 📊 Dataset

The dataset contains **1,000 loan applications** with the following original columns:

| Column | Description |
|---|---|
| `loan_id` | Unique loan application identifier |
| `age` | Applicant age |
| `income` | Applicant income |
| `loan_amount` | Requested loan amount |
| `credit_score` | Applicant credit score |
| `default` | Loan default indicator |

---

## 📊 Key Findings

### Data Quality

* 1,000 loan applications were analyzed.
* 51 income values were missing.
* 3 negative loan amounts were identified as invalid.
* Missing and invalid values were resolved without removing records.

### Outliers

* Extreme loan amounts were identified.
* A separate `loan_amount_cleaned` feature was created.
* Values were clipped between the 5th and 95th percentiles.
* All 1,000 records were retained.

### Feature Engineering

Three additional features were included in the final dataset:

```text
loan_amount_cleaned
dti_ratio
risk_category
```

### Risk Behavior

Default rates declined consistently from High Risk to Excellent applicants.

This suggests that credit-score-based risk segmentation provides useful information for understanding default behavior.

---

## 🌐 Streamlit Dashboard

The analysis was transformed into an interactive Streamlit web application.

The dashboard includes:

* 📊 Dataset summary
* 💳 Application statistics
* 📈 Default rate
* 💰 Average income
* 💵 Average loan amount
* 🎛️ Risk category filtering
* 📊 Default distribution
* 📈 Risk-category analysis
* 📉 Credit score vs. default analysis
* 📉 DTI ratio vs. default analysis
* 🔎 Applicant Explorer
* 📋 Dataset preview

### Live Application

👉 [https://loanriskanalysis-fsdruxvvfezgn4fa9ieffs.streamlit.app/](https://loanriskanalysis-fsdruxvvfezgn4fa9ieffs.streamlit.app/)

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **Streamlit**
* **Git**
* **GitHub**
* **Streamlit Community Cloud**

---

## 📁 Project Structure

```text
Loan_risk_analysis/
│
├── app.py
├── loan_data.csv
├── requirements.txt
├── Loan_Risk_Analysis_and_Feature_Engineering.ipynb
└── README.md
```

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Uzma-Jawed/Loan_risk_analysis.git
```

### 2. Navigate to the project folder

```bash
cd Loan_risk_analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📓 Notebook

The Jupyter Notebook contains the complete analysis workflow, including:

* Data loading
* Data inspection
* Missing-value analysis
* Data cleaning
* Outlier analysis
* Feature engineering
* Risk categorization
* Exploratory analysis
* Default-rate analysis
* Final dataset preparation

---

## 🚀 Project Outcome

This project demonstrates an end-to-end workflow for taking a raw dataset through:

```text
Raw Dataset
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Outlier Treatment
     ↓
Feature Engineering
     ↓
Risk Analysis
     ↓
Interactive Dashboard
     ↓
GitHub
     ↓
Live Deployment
```

The final dataset contains **zero missing values**, retains all original observations, and includes engineered features that support further risk analysis.

---

## 👩‍💻 Author

**Uzma Jawed**

GitHub:
[https://github.com/Uzma-Jawed](https://github.com/Uzma-Jawed)

Linkedin:
.[https://www.linkedin.com/in/uzma-jawed-21684728b/](https://www.linkedin.com/in/uzma-jawed-21684728b/)
