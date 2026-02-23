# salary_processing_system.py

def process_salaries(salaries, minimum_wage):
    # Remove salaries below minimum wage
    valid_salaries = [s for s in salaries if s >= minimum_wage]

    # Add 5% bonus to salaries > 50000
    updated_salaries = []
    for s in valid_salaries:
        if s > 50000:
            s += s * 0.05
        updated_salaries.append(round(s, 2))

    # Sort descending
    updated_salaries.sort(reverse=True)

    # Top 3 salaries
    top_3 = updated_salaries[:3]

    print("\nProcessed Salaries:", updated_salaries)
    print("Top 3 Highest Salaries:", top_3)


user_input = list(map(float, input("Enter employee salaries: ").split()))
min_wage = float(input("Enter minimum wage: "))
process_salaries(user_input, min_wage)