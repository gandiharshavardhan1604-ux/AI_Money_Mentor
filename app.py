import streamlit as st
import pandas as pd
import plotly.express as px
from utils import append_user_record, get_user_history

st.set_page_config(page_title="AI Money Mentor", layout="wide")

# ---------------- LOGIN / ACCOUNT ----------------
st.sidebar.header("👤 User Account")
username = st.sidebar.text_input("Enter Username")
password = st.sidebar.text_input("Enter Password", type="password")  # optional for now

login_button = st.sidebar.button("Enter")

if login_button and username:
    st.session_state["logged_in"] = True
    st.session_state["username"] = username

if "logged_in" not in st.session_state:
    st.warning("Please enter your account details to continue.")
    st.stop()  # stop execution until user logs in

username = st.session_state["username"]

# ---------------- HEADER ----------------
st.title("💰 AI Money Mentor")
st.caption(f"Welcome, {username}")
st.markdown("---")

# ---------------- USER INPUT ----------------
st.subheader("📊 Enter Your Financial Details")

col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Monthly Income (₹)", 10000, 1000000, 50000)
    goal_amount = st.number_input("Target Amount (₹)", 100000, 10000000, 2000000)
    years = st.slider("Time (Years)", 1, 30, 5)
with col2:
    risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])
    manual_expenses = st.number_input("Enter Monthly Expenses (₹)", 0, income, 30000)

# ---------------- EXPENSE UPLOAD ----------------
st.subheader("📥 Upload Your Expenses (Optional)")
uploaded_file = st.file_uploader("Upload CSV with columns: Category, Amount", type=["csv"])
if uploaded_file:
    expense_df = pd.read_csv(uploaded_file)
    if "Category" in expense_df.columns and "Amount" in expense_df.columns:
        total_expenses = expense_df["Amount"].sum()
        expenses = total_expenses
        st.success(f"Total Expenses from CSV: ₹{total_expenses}")
        fig_expense = px.pie(expense_df, values="Amount", names="Category", title="Expense Breakdown")
        st.plotly_chart(fig_expense, use_container_width=True)
    else:
        st.error("CSV must contain 'Category' and 'Amount' columns.")
else:
    expenses = manual_expenses

# ---------------- CALCULATIONS ----------------
savings = income - expenses
emergency_fund = expenses * 6
r = 0.12 / 12
n = years * 12
sip = goal_amount * r / ((1 + r)**n - 1)

alloc = {"Low": [40, 50, 10], "Medium": [60, 30, 10], "High": [80, 10, 10]}[risk]

# ---------------- KPI ----------------
st.subheader("📊 Financial Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Monthly Savings", f"₹{savings}", delta=f"{round((savings/income)*100)}%")
col2.metric("Emergency Fund", f"₹{emergency_fund}")
col3.metric("Required SIP", f"₹{int(sip)}")

# ---------------- CHARTS ----------------
st.subheader("📈 Investment Insights")
col4, col5 = st.columns(2)

# Portfolio allocation chart
df_alloc = pd.DataFrame({"Category": ["Equity", "Debt", "Gold"], "Allocation": alloc})
fig1 = px.pie(df_alloc, values="Allocation", names="Category", title="Recommended Portfolio Allocation")
col4.plotly_chart(fig1, use_container_width=True)

# Wealth growth chart
months = list(range(1, n+1))
values = []
total = 0
for month in months:
    total = total * (1 + r) + sip
    values.append(total)

growth_df = pd.DataFrame({"Month": months, "Wealth": values})
fig2 = px.line(growth_df, x="Month", y="Wealth", title="Projected Wealth Growth")
col5.plotly_chart(fig2, use_container_width=True)

# ---------------- INSIGHTS ----------------
st.subheader("🤖 Smart Insights")
if savings <= 0:
    st.error("⚠️ You are spending more than you earn.")
elif savings < income * 0.2:
    st.warning("⚠️ Try to save at least 20% of your income each month.")
else:
    st.success("✅ Great! You have a healthy savings habit.")

if sip > savings:
    st.warning("⚠️ Your goal may be aggressive. Increase savings or extend timeline.")
else:
    st.success("🎯 Your financial goal is achievable.")

# ---------------- SAVE USER RECORD ----------------
record = {
    "income": income,
    "expenses": expenses,
    "savings": savings,
    "goal": goal_amount,
    "years": years,
    "risk": risk,
    "sip": int(sip)
}
append_user_record(username, record)

# ---------------- FREE AI CHAT ----------------
st.subheader("💬 Ask AI Money Mentor")
user_query = st.text_input("Ask a financial question:")

def free_ai_answer(query):
    query = query.lower()
    if "save" in query or "saving" in query:
        return "💡 Save at least 20% of your income and reduce unnecessary expenses."
    elif "invest" in query or "investment" in query:
        return "📈 Invest in SIPs, mutual funds, or fixed deposits. Diversify across equity, debt, and gold."
    elif "risk" in query:
        return "⚖️ Higher risk = more equity exposure, Lower risk = more debt exposure."
    elif "goal" in query:
        return "🎯 Adjust your investment or extend your timeline to meet your financial goal."
    elif "expense" in query or "budget" in query:
        return "📊 Track your expenses and cut non-essential spending."
    else:
        return "🤖 Ask about savings, investments, risk, expenses, or goals."

if user_query:
    st.info(free_ai_answer(user_query))

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built by GANDI HARSHA VARDHAN - Fully Free Version 🚀")