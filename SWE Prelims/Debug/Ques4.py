#Study the Multiplication Table Above 
print("""
    General Multiplication Table
  """)
for i in range (1, 11):
  for j in range (1,13):
    print(i, "x", j , "=" , i * j)
  print("\n")#To Print Space 



#Now Debug This
print("""
      Custom Multiplication Table 
""")

user_choice = input(int("Enter the num to display the multiplication table: "))
print("\n") #To Print Space 
while user_choice < 0:
  print("Please Enter a positive number")
  user_choice = int(input("Re-enter the num to display the multiplication table: "))
  print("\n") #To Print Space 

for i in range(13):
  print(f"{user_choice x i} = {user_choice * i}")
  
print("\n") #To Print Space 