
while(True):
    ask_input = input("Please input here:")
    if ask_input == "no-print":
        continue
    elif ask_input == "exit-no-print":
        break
    print("Your input was: " + ask_input)
    if ask_input == "exit":
        print("Done")
        break

