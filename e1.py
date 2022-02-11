
onoff = True
while onoff:
        
    print("****WELCOME TO FERMAT'S PRIME CHECKER****")

    number_to_check = input("Please input a number to check if it is a fermat's prime\n===>")

    if number_to_check.isnumeric:
            
        number_to_check = int(number_to_check)
        is_prime = True

        for i in range(2,number_to_check):

            if number_to_check % i == 0:

                print("The number is not prime")
                is_prime = False
                break
        
        if is_prime:

            exp = 1

            while exp < number_to_check:

                if 2**2**exp + 1 == number_to_check:

                    print(f"The Number {number_to_check} is a Fermat's prime\n")
                    break

                elif 2**2**exp + 1 > number_to_check:

                    print(f"The Number {number_to_check} is a Fermat's prime\n")
                    break
                
                else:
                    exp += 1


        while True:

            option = input("**PRESS 0 TO CALCULATE ANTOHER NUMBER AND 1 TO EXIT THE CALCULATOR**\n===>")

            if option.isnumeric:

                option = int(option)

                if option == 1:

                    print ("Goodbye")
                    onoff = False
                    break

                elif option == 0:

                    print ("Restarting program for another number to calculate")
                    break

                else:

                    print ("Please enter one of the two nubers as options")
            else:

                print ("INVALID INPUT")

    else:
        print ("INVALID INPUT")
