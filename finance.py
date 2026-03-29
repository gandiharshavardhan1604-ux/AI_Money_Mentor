def calculate_savings(income, expenses):
    return income - expenses

def calculate_emergency_fund(expenses):
    return expenses * 6

def calculate_sip(goal_amount, years, rate=0.12):
    n = years * 12
    r = rate / 12
    return goal_amount * r / ((1 + r)**n - 1)

def risk_allocation(risk):
    return {"Low": [40, 50, 10], "Medium": [60, 30, 10], "High": [80, 10, 10]}[risk]