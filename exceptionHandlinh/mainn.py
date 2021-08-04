x = input("Enter the frist Number:")
y = input("Enter the 2nd Number:")
z = 0


try:
    z = x / int(y)
    print(z)
except ZeroDivisionError as e:
    print(e)
# if exception is known: aslo multiple exception handles in that way
except Exception as e:
    print("Type of Exception"+type(e).__name__)
finally:
    print("In Final Block")