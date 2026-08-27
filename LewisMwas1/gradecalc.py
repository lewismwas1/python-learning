name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >=50:
    grade = "D"
else :
    grade = "F"
print(f"Hello {name} ! Your grade is {grade}.")
if grade =="A":
    print("Excellent work!")
elif grade == "B":
    print("Very Good!")
elif grade == "C":
    print("Good Effort")
elif grade == "D":
    print("Keep Trying!")
elif grade == "F":
    print("You need to keep practicing!")