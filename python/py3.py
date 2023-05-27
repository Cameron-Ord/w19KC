try:
    num = input("Input a number")
    num = int(num)
    test = 2 + num

except TypeError:
    print("you cant mix and match types")

except:
    print("something has gone wrong")

finally:
    print("I will run no matter what")

choice = input("Please enter your name:")
print("Hello", choice)