# Task 2
# Implement a bubble sort function

def bubble(list):
    temp = 0 #for storing one of the elements while switching
    control = 1 #control variable to indicate when to stop searching - amount of element switchings performed
    while control > 0: #while at least one element switching has occured in the previous cycle
        control = 0 #each cycle setting the control value to zero
        for x in range(0,len(list)):
            if x == len(list) - 1: #we avoid performing anything with the last element, because x+1 doesn't exist for it
                break
            if list[x] > list[x+1]:
                temp = list[x+1] #temporarily store the value that we switch so it doesnt get lost
                list[x+1] = list[x]
                list[x] = temp
                print(list)
                control += 1
                print(control)

list = [9,11,1,2,3,4,9,5,6,7,8,9,9,4,7,6]
bubble(list)
print(list)
