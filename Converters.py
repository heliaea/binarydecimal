def binary_to_decimal(b):
    b_list = [int(i) for i in b]

    total = 0

    for index, binary in enumerate(reversed(b_list)):

        if binary == 1:
            total += (2 ** index)

    return total

def decimal_to_binary(d):
    total = 0
    iterations = 0

    while total < d:
        total += 2 ** iterations
        iterations += 1

    b = []

    for i in reversed(range(iterations)):
        if d - (2 ** i) >= 0:
            d -= (2 ** i)
            b.append(1)
        else:
            b.append(0)

    return ''.join([str(i) for i in b])

def conversion():
    while True:
        cont = True

        print(
            "1. Decimal to Binary\n"
            "2. Binary to Decimal\n"
            "3. Exit"
        )

        choice = int(input(">> "))

        if choice == 3:
            print("Exiting...")
            exit()

        if not (choice == 1 or choice == 2):
            print("Invalid Input!\n")
            continue

        prompts = {
            1: "\nInput a decimal number",
            2: "\nInput a binary number"
        }

        if choice == 1:
            user_input = int(input(prompts[choice] + "\n>> "))
            print("\n", user_input, " in binary is:\n", decimal_to_binary(user_input), sep='')
    
        elif choice == 2:
            user_input = input(prompts[choice] + "\n>> ")

            for i in user_input:
                if not (i == '0' or i == '1'):
                    print("Invalid Input!\n")
                    cont = False
                    break
            
            if cont:
                print("\n", user_input, " in decimal is:\n", binary_to_decimal(user_input), sep='')

        print()