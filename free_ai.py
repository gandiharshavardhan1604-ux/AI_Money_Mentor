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