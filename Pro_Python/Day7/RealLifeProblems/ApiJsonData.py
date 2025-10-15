import json


large_data = '''{
    "employees": [
        {"id": 1, "name": "Harman", "role": "Software Engineer",
        "salary": 75000},
        {"id": 2, "name": "Priya", "role": "Data Scientist", "salary": 80000},
        {"id": 3, "name": "Arjun", "role": "DevOps Engineer", "salary": 70000}
    ],
    "company": "Tech Corp",
    "location": "Bangalore"
}'''

parsed = json.loads(large_data)

print(f"Company: {parsed['company']}")
print(f"Location: {parsed['location']}")
print("\nEmployees:")

print(json.dumps(parsed['employees'], indent=2))
