students = {
    "Harman": {"Math": 90, "English": 85},
    "Sahil": {"Math": 80, "English": 88},
    "Ayushi": {"Math": 92, "English": 91}
}

students["Sahil"]["Science"] = 93

avg = sum(students["Sahil"].values()) / len(students["Sahil"])
print("Sahil Averaga: ", avg)
