import streamlit as st
import pandas as pd

# Initialize session state for expenses if it doesn't exist
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# App Header
st.title("💰 Personal Budget Tracker")

# 1. & 2. Input Form
st.header("Add a New Expense")

with st.form("expense_form", clear_on_submit=True):
    date = st.date_input("Date")
    item = st.text_input("Expense Item")
    amount_str = st.text_input("Amount Spent (RM)")
    submit_button = st.form_submit_button("Add Expense")

    if submit_button:
        # 3. Exception Handling for validation
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("The amount cannot be negative.")
            
            # Save the expense
            new_expense = {
                "Date": date,
                "Expense Item": item,
                "Amount Spent (RM)": amount
            }
            st.session_state.expenses.append(new_expense)
            st.success(f"✅ Expense '{item}' added successfully!")
            
        except ValueError:
            st.error("⚠️ Please enter a valid positive number for the amount.")

# 4. Display Summary
st.header("Expense Summary")

if st.session_state.expenses:
    # Create DataFrame for display
    df = pd.DataFrame(st.session_state.expenses)
    
    # Display the table
    st.table(df)
    
    # Calculate and display total
    total = df["Amount Spent (RM)"].sum()
    st.markdown(f"### Total Expenses: RM {total:.2f}")
else:
    st.info("No expenses recorded yet.")