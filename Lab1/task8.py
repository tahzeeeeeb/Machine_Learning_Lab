employees = [
    {"name": "Ali", "department": "Sales", "salary": 45000},
    {"name": "Sara", "department": "IT", "salary": 72000},
    {"name": "Omar", "department": "Sales", "salary": 58000},
    {"name": "Hina", "department": "HR", "salary": 51000}
]

highestEmployee = employees[0]

for employee in employees:
    if employee["salary"] > highestEmployee["salary"]:
        highestEmployee = employee

print("Highest paid employee:", highestEmployee["name"])
print("Department:", highestEmployee["department"])
print("Salary:", highestEmployee["salary"])
