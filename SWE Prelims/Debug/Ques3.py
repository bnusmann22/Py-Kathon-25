#Result grader
exam_score = float(input("Enter Exam Score: "))
while exam_score < 0 and exam_score > 100:
  print("Invalid Exam score")
  exam_score= float(input("re-Enter your exams score: "))

if exam_score <= 30: