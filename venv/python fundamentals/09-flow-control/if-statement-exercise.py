ask_number = int(input('Give a number from 1 to 7'))

if ask_number == 1:
    print("You chose Monday")
elif ask_number < 1:
    print("There ar eno negative number days!")
elif ask_number > 7:
    print("There are only 7 days in a week!")
else:
    print("This number means nuthin")