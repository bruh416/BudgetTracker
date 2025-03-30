import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title(" Budget Tracker")

st.sidebar.header("Enter Your Financial Details")
income = st.sidebar.number_input("Enter your monthly income:", min_value=0)
expense = st.sidebar.number_input("Enter your total expenses:", min_value=0)
expense_category = st.sidebar.text_input("Expense Category (e.g., Rent, Food, Bills)")

# Store Transactions
if "transactions" not in st.session_state:
    st.session_state.transactions = []

if st.sidebar.button("Add Expense"):
    st.session_state.transactions.append({"Category": expense_category, "Expense": expense})
    st.success("Expense added!")

# Convert Transactions to DataFrame
df = pd.DataFrame(st.session_state.transactions)

# Display Budget Summary
st.subheader(" Budget Summary")
st.write(f" **Income:** ${income}")
st.write(f" **Total Expenses:** ${df['Expense'].sum() if not df.empty else 0}")
st.write(f" **Remaining Balance:** ${income - df['Expense'].sum() if not df.empty else income}")

# Expense Chart
if not df.empty:
    fig, ax = plt.subplots()
    ax.pie(df['Expense'], labels=df['Category'], autopct="%1.1f%%")
    st.pyplot(fig)
