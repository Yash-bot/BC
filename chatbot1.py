def get_recommendation(risk_tolerance, financial_goal, time_horizon, sustainability_interest):
    recommendations = {
        "Conservative": {
            "Retirement": {
                "0-10 years": {
                    "No": "60% in bonds, 30% in conservative mutual funds, 10% in cash or high-quality stocks",
                    "Yes": "60% in green bonds, 30% in ESG-focused conservative mutual funds, 10% in sustainable money market funds"
                },
                "10-15 years": {
                    "No": "50% in bonds, 40% in conservative mutual funds, 10% in cash or high-quality stocks",
                    "Yes": "50% in green bonds, 40% in ESG-focused conservative mutual funds, 10% in sustainable stocks"
                },
                "15-20 years": {
                    "No": "40% in bonds, 40% in conservative mutual funds, 20% in cash or high-quality stocks",
                    "Yes": "40% in green bonds, 40% in ESG-focused conservative mutual funds, 20% in sustainable stocks"
                }
            },
            "Buying a House": {
                "0-10 years": {
                    "No": "70% in bonds, 20% in conservative mutual funds, 10% in cash",
                    "Yes": "70% in green bonds, 20% in ESG-focused conservative mutual funds, 10% in sustainable money market funds"
                },
                "10-15 years": {
                    "No": "60% in bonds, 30% in conservative mutual funds, 10% in cash",
                    "Yes": "60% in green bonds, 30% in ESG-focused conservative mutual funds, 10% in sustainable stocks"
                },
                "15-20 years": {
                    "No": "50% in bonds, 40% in conservative mutual funds, 10% in cash",
                    "Yes": "50% in green bonds, 40% in ESG-focused conservative mutual funds, 10% in sustainable stocks"
                }
            },
            "Education": {
                "0-10 years": {
                    "No": "50% in bonds, 30% in balanced mutual funds, 20% in cash",
                    "Yes": "50% in green bonds, 30% in ESG-focused balanced mutual funds, 20% in sustainable money market funds"
                },
                "10-15 years": {
                    "No": "40% in bonds, 40% in balanced mutual funds, 20% in high-quality stocks",
                    "Yes": "40% in green bonds, 40% in ESG-focused balanced mutual funds, 20% in sustainable stocks"
                },
                "15-20 years": {
                    "No": "30% in bonds, 50% in balanced mutual funds, 20% in high-quality stocks",
                    "Yes": "30% in green bonds, 50% in ESG-focused balanced mutual funds, 20% in sustainable high-growth stocks"
                }
            }
        }
    }

    # Validate inputs
    if risk_tolerance not in recommendations:
        return "Invalid risk tolerance."
    if financial_goal not in recommendations[risk_tolerance]:
        return "Invalid financial goal."
    if time_horizon not in recommendations[risk_tolerance][financial_goal]:
        return "Invalid time horizon."
    if sustainability_interest not in recommendations[risk_tolerance][financial_goal][time_horizon]:
        return "Invalid sustainability interest."

    # Get the recommendation
    recommendation = recommendations[risk_tolerance][financial_goal][time_horizon][sustainability_interest]
    return recommendation

def main():
    print("Welcome to the Robo-Advisor Chatbot!")

    # Get user details
    name = input("Please enter your name: ")
    risk_tolerance = input("Enter your risk tolerance (Conservative, Moderate, Aggressive): ").capitalize()
    financial_goal = input("Enter your financial goal (Retirement, Buying a House, Education): ").capitalize()
    time_horizon = input("Enter your time horizon (0-10 years, 10-15 years, 15-20 years): ")
    sustainability_interest = input("Are you interested in sustainable investments? (Yes, No): ").capitalize()

    # Get recommendation
    recommendation = get_recommendation(risk_tolerance, financial_goal, time_horizon, sustainability_interest)
    
    # Print personalized recommendation
    print(f"\nHello {name}, based on your inputs, we recommend the following investment strategy:")
    print(recommendation)

if __name__ == "__main__":
    main()
