import pickle

with open("student.pkl", "rb") as file:
    data = pickle.load(file)

print(f"Got the data: {data}")
print("Name:", data["name"])
