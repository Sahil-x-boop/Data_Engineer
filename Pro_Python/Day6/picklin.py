import pickle

student = {
    "name": "Harman",
    "age": 24,
    "skills": ["Python", "Java", "Spring Boot"]
}


with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print("Pickling Done! Data saved to student.pkl")
