def get_dec_from_user():
    try:
        num = input("enter a number")
        num = float(num)
        return num
    except ValueError:
        print("please enter a number")
    except:
        print("something went wrong")

while(True):

    num_one = get_dec_from_user()
    num_two = get_dec_from_user()

    if(num_one == None or num_two == None):
        print("something went wrong")
    else:
        break


added_nums = num_one + num_two
print(added_nums)