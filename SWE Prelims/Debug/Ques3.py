#Result grader
exam_score = input(int("Enter Your Score: "))

while exam_score < 0 and exam_score > 100:
    print("Invalid Input")
    exam_score = int(input("Re-Enter Your Score: "))

if exam_score >= 80:
    return grade = "A"
elif exam_score >= 60 and exam_score < 80:
    return grade = "B"
elif exam_score > 50 or exam_score <= 60:
    return grade = "C"
elif exam_score > 40 and exam_score <= 50:
    return grade = "D"
else:
    return grade = "E"

print(f"You got a {grade}")
