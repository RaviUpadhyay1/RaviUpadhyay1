marks = int(input("Enter a marks:"))
if marks>=90:
   grade = "A+"
elif marks>=80:
   grade = "A"
elif marks>=70:
   grade = "B"
elif marks>=60:
   grade = "C"
elif marks>=50:
   grade = "D"
else:
    grade = "Fail"
print("Your grade is " + grade)