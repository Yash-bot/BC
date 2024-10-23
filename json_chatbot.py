import json

def load_recommendations(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_recommendation(data, risk_tolerance, financial_goal, time_horizon, sustainability_interest):
    try:
                # Validate inputs
        if risk_tolerance not in data:
            return "Invalid risk tolerance."
        if financial_goal not in data[risk_tolerance]:
            return "Invalid financial goal."
        if time_horizon not in data[risk_tolerance][financial_goal]:
            return "Invalid time horizon."
        if sustainability_interest not in data[risk_tolerance][financial_goal][time_horizon]:
            return "Invalid sustainability interest."
        return data[risk_tolerance][financial_goal][time_horizon][sustainability_interest]
    except KeyError:
        return "Recommendation not found."

# Usage
recommendations_data = load_recommendations('advisor.json')
risk_tolerance = input("Enter your risk tolerance (Conservative, Moderate, Aggressive): ").capitalize()
financial_goal = input("Enter your financial goal (Retirement, Buying a House, Education): ").capitalize()
time_horizon = input("Enter your time horizon (0-10 years, 10-15 years, 15-20 years): ")
sustainability_interest = input("Are you interested in sustainable investments? (Yes, No): ").capitalize()


recommendation = get_recommendation(recommendations_data,risk_tolerance,financial_goal,time_horizon,sustainability_interest)
print(recommendation)
