import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Loan Risk Analysis",
    page_icon="💳",
    layout="wide"
)


# --------------------------------------------------
# Load and Prepare Data
# --------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("loan_data.csv")

    # Handle missing income
    income_median = df["income"].median()
    df["income"] = df["income"].fillna(income_median)

    # Handle invalid negative loan amounts
    df.loc[df["loan_amount"] < 0, "loan_amount"] = np.nan

    loan_amount_median = df["loan_amount"].median()
    df["loan_amount"] = df["loan_amount"].fillna(loan_amount_median)

    # Outlier treatment
    lower_limit = df["loan_amount"].quantile(0.05)
    upper_limit = df["loan_amount"].quantile(0.95)

    df["loan_amount_cleaned"] = df["loan_amount"].clip(
        lower=lower_limit,
        upper=upper_limit
    )

    # Feature engineering
    df["dti_ratio"] = (
        df["loan_amount_cleaned"] / df["income"]
    )

    # Credit risk categories
    bins = [299, 579, 669, 739, 850]
    labels = ["High Risk", "Fair", "Good", "Excellent"]

    df["risk_category"] = pd.cut(
        df["credit_score"],
        bins=bins,
        labels=labels
    )

    return df


df = load_data()


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("💳 Loan Risk Analysis Dashboard")

st.markdown(
    """
    Explore loan applicant characteristics, credit-risk categories,
    and default behavior through interactive analysis.
    
    **Dataset:** Synthetic loan applicant data for educational purposes.
    """
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

risk_options = ["All"] + df["risk_category"].dropna().unique().tolist()

selected_risk = st.sidebar.selectbox(
    "Risk Category",
    risk_options
)

if selected_risk == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["risk_category"] == selected_risk
    ].copy()


# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------

total_applicants = len(filtered_df)

defaulted = filtered_df["default"].sum()

default_rate = (
    filtered_df["default"].mean() * 100
    if total_applicants > 0
    else 0
)

average_income = (
    filtered_df["income"].mean()
    if total_applicants > 0
    else 0
)

average_loan = (
    filtered_df["loan_amount_cleaned"].mean()
    if total_applicants > 0
    else 0
)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Applications",
    f"{total_applicants:,}"
)

col2.metric(
    "Default Rate",
    f"{default_rate:.2f}%"
)

col3.metric(
    "Average Income",
    f"${average_income:,.0f}"
)

col4.metric(
    "Average Loan Amount",
    f"${average_loan:,.0f}"
)


st.divider()


# --------------------------------------------------
# Default Distribution
# --------------------------------------------------

st.subheader("Default Distribution")

default_counts = filtered_df["default"].value_counts().sort_index()

default_labels = {
    0: "No Default",
    1: "Default"
}

default_display = default_counts.rename(
    index=default_labels
)

fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(
    default_display.index,
    default_display.values
)

ax.set_xlabel("Loan Status")
ax.set_ylabel("Number of Applicants")
ax.set_title("Loan Default Distribution")

st.pyplot(fig)


# --------------------------------------------------
# Default Rate by Risk Category
# --------------------------------------------------

st.subheader("Default Rate by Risk Category")

risk_order = [
    "High Risk",
    "Fair",
    "Good",
    "Excellent"
]

risk_default_rate = (
    df.groupby(
        "risk_category",
        observed=False
    )["default"]
    .mean()
    .reindex(risk_order)
    * 100
)

fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(
    risk_default_rate.index,
    risk_default_rate.values
)

ax.set_xlabel("Risk Category")
ax.set_ylabel("Default Rate (%)")
ax.set_title("Default Rate by Credit Risk Category")

st.pyplot(fig)


# --------------------------------------------------
# Credit Score Analysis
# --------------------------------------------------

st.subheader("Credit Score vs Default")

fig, ax = plt.subplots(figsize=(8, 4))

df.boxplot(
    column="credit_score",
    by="default",
    ax=ax
)

ax.set_xlabel("Default (0 = No, 1 = Yes)")
ax.set_ylabel("Credit Score")
ax.set_title("Credit Score by Default Status")

plt.suptitle("")

st.pyplot(fig)


# --------------------------------------------------
# DTI Analysis
# --------------------------------------------------

st.subheader("DTI Ratio vs Default")

fig, ax = plt.subplots(figsize=(8, 4))

df.boxplot(
    column="dti_ratio",
    by="default",
    ax=ax
)

ax.set_xlabel("Default (0 = No, 1 = Yes)")
ax.set_ylabel("Loan Amount / Income")
ax.set_title("DTI Ratio by Default Status")

plt.suptitle("")

st.pyplot(fig)


# --------------------------------------------------
# Applicant Explorer
# --------------------------------------------------

st.divider()

st.subheader("🔎 Applicant Explorer")

loan_ids = filtered_df["loan_id"].tolist()

selected_loan_id = st.selectbox(
    "Select a Loan ID",
    loan_ids
)

applicant = filtered_df[
    filtered_df["loan_id"] == selected_loan_id
].iloc[0]


col1, col2, col3 = st.columns(3)

col1.metric(
    "Age",
    f"{applicant['age']:.0f}"
)

col1.metric(
    "Income",
    f"${applicant['income']:,.0f}"
)

col2.metric(
    "Loan Amount",
    f"${applicant['loan_amount_cleaned']:,.0f}"
)

col2.metric(
    "Credit Score",
    f"{applicant['credit_score']:.0f}"
)

col3.metric(
    "DTI Ratio",
    f"{applicant['dti_ratio']:.2f}"
)

col3.metric(
    "Risk Category",
    str(applicant["risk_category"])
)


if applicant["default"] == 1:
    st.warning("⚠️ This applicant defaulted.")
else:
    st.success("✅ This applicant did not default.")


# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------

st.divider()

st.subheader("📋 Dataset Preview")

display_columns = [
    "loan_id",
    "age",
    "income",
    "loan_amount",
    "loan_amount_cleaned",
    "credit_score",
    "dti_ratio",
    "risk_category",
    "default"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Loan Risk Analysis | Educational project using synthetic data"
)