import random

from registerVoter import Register

# FUNCTIONS
# ======================================================================================================================

def optionDescription():
    print("\n------------- VOTER'S REGISTRATION FORM -------------")
    print("| Please fill in the necessary forms for registration.")

# MAIN()
# ======================================================================================================================

while True:
    print("\nOnline Voting System")
    print("=============== ONLINE VOTING SYSTEM ===============")
    print("[A] ========== Register Voter\n[B] ========== Cast Vote")
    print("[C] ========== View Candidate List\n[D] ========== View Registered Voters List")
    print("[E] ========== Exit Program")

    option = input("| Please select from the following options: ").strip().upper()

    match option:
        case "A":
            print(f"\nYou Selected: {option}")
            optionDescription()
            fname = input("First Name: ")
            lname = input("Last Name: ")

            randNum = random.randint(1,999)
            randnumtostr = str(randNum)
            letters = ['A','B','C','D','E','F','G','H','I','J','K',
                       'L','M','N','O','P','R','S','T','U','V','W',
                       'X','Y','Z']

            randLettersA = random.choice(letters)
            randLettersB = random.choice(letters)
            randLettersC = random.choice(letters)
            randLettersD = random.choice(letters)
            randLettersE = random.choice(letters)
            randLettersF = random.choice(letters)

            id = (randnumtostr + randLettersA + "-" + randLettersB + randLettersC
                  + randLettersD + "-" + randnumtostr + randLettersE + randLettersF)

            voter = Register(fname, lname, id)
            voter.showAndUpdateInfo()

        case "B":
            print("B")


        case "C":
            print('C')


        case "D":
            print('D')


        case "E":
            print('E')
            break


        case _:
            print("Invalid input.")