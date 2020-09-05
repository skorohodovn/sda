
while(True):
    input_string = input("Please input a string")
    if len(input_string) < 10:
        print("The string you provided is less than 10 characters long!")
        break
    if (len(input_string)%2 == 0):
        print("The string's length is even!")
        mid_num = len(input_string)//2
    else:
        print("The string's length is odd!")
        mid_num = len(input_string)//2
        print(input_string[mid_num])
        print(input_string[mid_num-2:mid_num+2+(len(input_string//2))])