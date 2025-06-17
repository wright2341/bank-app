import streamlit as st
from home import Savingsaccount

st.set_page_config(page_title ="savings acc" layout ="centered")
savings = savings account (200000)


with st.from("savings_form"):
    amount = st.number_imput("Enter Amount")
    operations = st.selectbox("Deposit or Withdraw")
    submit = st.from_submt_button("Submit")

if submit:
    with st.spinner("Processing..."):
        if operation == "Withdraw":
            savings.withdraw(amount)
        else:
            savings.deposit(amount)
st.success("Transaction complete. New Balance:{savings.balance}") 

