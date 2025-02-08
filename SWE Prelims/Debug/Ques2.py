
print("""
        Voter Eligibility
    Check Your Eligibility Status 🙂
""")

user_age = input("Enter Your age: ")

while user_age < 1 or user_age > 100:
  print("Invalid Age")
  user_age = int(input("Re-Enter Your age: "))

if user-age > 18:
  print("Congrats , You Eligible to vote 🚀)
else:
  print("Sorry , You are too young to vote")