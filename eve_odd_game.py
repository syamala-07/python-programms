while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
    choice = input("Do you want to continue? (yes/no): ")
    if choice == "no":
        print("Game Over")
        break