students = [
    {"name": "Alice", "age": 17, "grade": 85},
    {"name": "Bob", "age": 19, "grade": 90},
    {"name": "Charlie", "age": 18, "grade": 75},
    {"name": "David", "age": 20, "grade": 95},
    {"name": "Eva", "age": 22, "grade": 88}
]
def checkMinor(student):
    
    a = lambda b : b <= 18
    if a(student.get("age")) == True:
        return student.get("name")
minors = list(filter( lambda s : s["age"] <= 18, students)) 
print(minors)