# This program displays the steps to follow to disassemble an acme dryer

# The main function displays the program's main logic
def main():
    # Display start up message
    startup_message()
    input('Press enter to see Step1 ')
    # Display step 1
    step1()
    input('Press Enter to see Step2 ')
    # Display step2
    step2()
    input('Press Enter to see Step3 ')
    # Display step 3
    step3()
    input('Press Enter to see Step 4 ')
    # Display step 4
    step4()

# The startup_message function displays a message to the user
# The program's initial message written on screen
def startup_message():
     print('This program tells you how to ')
     print(' disassemble an ACME laundry dryer.')
     print('There are four steps in the process.')

# Step1
def step1():
    print('Step 1: Unplug the dryer and')
    print('move it away from the wall.')
    print()

# Step2
def step2():
    print('Step 2: Remove the six screws')
    print('from the back of the dryer.')
    print()

# Step3
def step3():
    print('Step 3: Remove the back panel')
    print('from the dryer.')
    print()

def step4():
    print('Step 4: Pull the top of the')
    print('dryer straight up.')


# Call the main function to begin the program
main()
