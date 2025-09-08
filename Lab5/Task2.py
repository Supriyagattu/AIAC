# Loan approval logic for different applicants

def approve_loan(applicant):
    # Example AI-generated logic (for demonstration purposes)
    if applicant['name'].lower() == 'john':
        return "Approved"
    elif applicant['name'].lower() == 'priya':
        return "Denied"
    else:
        # Generic logic based on income
        if applicant['income'] > 50000:
            return "Approved"
        else:
            return "Denied"

# Applicants
applicants = [
    {'name': 'John', 'gender': 'Male', 'income': 40000},
    {'name': 'Priya', 'gender': 'Female', 'income': 60000},
    {'name': 'Alex', 'gender': 'Male', 'income': 70000},
    {'name': 'Sara', 'gender': 'Female', 'income': 30000}
]

# Evaluate loan approvals
for applicant in applicants:
    result = approve_loan(applicant)
    print(f"Applicant: {applicant['name']}, Gender: {applicant['gender']}, Income: {applicant['income']} -> Loan: {result}")

# Evaluation of bias:
print("\nEvaluation:")
print("The logic above approves or denies loans based on the applicant's name for 'John' and 'Priya', regardless of their income.")
print("This exhibits bias, as different criteria are applied based on the name, which may correlate with gender or ethnicity.")
print("For other applicants, the decision is based on income, which is a more objective criterion.")