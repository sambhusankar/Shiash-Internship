# Task 2
# If ans else condition
def Quiz():
    print("Who developed python ?")
    print(" 1. Guido Van Rossum \n 2. Dennis Ritchie \n 3. james Arthur \n 4. Brendan Eich")
    ans = input("Ans :  ")
    if ans == "Guido Van Rossum":
        print("Right Answer")
    else:
        print("You are wrong the right answer is Guido Van Rossum" )

Quiz()

# If elif and else condition

# Asking user for their age
def GetAge():
    age = int(input("Please enter your age: "))

    # Checking age and providing a message
    if age < 0:
        print("Invalid age! Please enter a valid age.")
    elif age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
GetAge()