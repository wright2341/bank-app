import streamlit as st

class Account:
    def __init__(self, balance=10000000):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class SavingsAccount(Account):
    WITHDRAWAL_LIMIT = 20000  # limit per withdrawal

    def withdraw(self, amount):
        if amount > self.WITHDRAWAL_LIMIT:
            return False
        return super().withdraw(amount)

class CurrentAccount(Account):
    pass


st.set_page_config(page_title="Nova Bank")
st.title("Nova Bank")

account_type = st.sidebar.selectbox("Select Account Type", ("Savings", "Current"))
action = st.sidebar.radio("Choose Action", ("Deposit", "Withdraw"))

if 'savings' not in st.session_state:
    st.session_state.savings = SavingsAccount()
if 'current' not in st.session_state:
    st.session_state.current = CurrentAccount()

amount = st.number_input("Enter Amount", min_value=1.0, format="%.2f")

account = st.session_state.savings if account_type == "Savings" else st.session_state.current

if st.button("Submit"):
    if action == "Deposit":
        success = account.deposit(amount)
        if success:
            st.success(f"Successfully deposited ${amount:.2f} to your {account_type} account.")
        else:
            st.error("Deposit failed. Amount must be positive.")
    elif action == "Withdraw":
        success = account.withdraw(amount)
        if success:
            st.success(f"Successfully withdrew ${amount:.2f} from your {account_type} account.")
        else:
            if account_type == "Savings" and amount > SavingsAccount.WITHDRAWAL_LIMIT:
                st.error(f"Withdrawal failed. Limit per transaction is ${SavingsAccount.WITHDRAWAL_LIMIT} for Savings Account.")
                st.warning(f"🔔 Debit Alert: ${amount:.2f} has been deducted from your {account_type} account.")
            else:
                st.error("Withdrawal failed. Check your balance or amount.")

st.write(" Account Balances")
st.write(f"Savings Account Balance: ${st.session_state.savings.balance:.2f}")
st.write(f"Current Account Balance: ${st.session_state.current.balance:.2f}")