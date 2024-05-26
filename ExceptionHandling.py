try:
    a = int(input("Enter a number : "))
    b = int(input("Enter second number : "))
    c = a + b
except Exception as e:
    print(e)

else:
    print(c)
finally:
    print("end")