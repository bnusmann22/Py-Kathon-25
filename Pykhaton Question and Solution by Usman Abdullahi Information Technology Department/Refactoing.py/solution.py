def func():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {'an adult' if age >= 18 else 'you are not an adult'}.")

func()
