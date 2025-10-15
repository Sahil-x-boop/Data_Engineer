
scores = {"Harman": 88, "Sahil": 92, "Shubham": 95, "Gurmeet": 85}


topper = max(scores, key=scores.get)
print(topper)

print(f"Topper is {topper} with marks: {scores[topper]}")
