# Fizz Buzzz Challenge 

n = input(int("Enter a number: "))

def fizzbuzz(n):
  for i in range (1, n+1):
    if i%3 == 0 or i %5 ==0:
      print("FizzBuzz")
    else i%3 == 0:
      print("Fizz")
    else i%5 == 0:
      print("Buzz")
    else:
      print(i)
