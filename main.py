import random

from listOfVoters import ViewList
from registerVoter import Register

# FUNCTIONS
# ======================================================================================================================

def optionDescriptionA():
    print("\n------------- VOTER'S REGISTRATION FORM -------------")
    print("| Please fill in the necessary forms for registration.")

def optionDescriptionD():
    print("\n------------- REGISTERED VOTER'S LIST -------------")
    print("| The following is the list of people")
    print("| registered to vote.")

# MAIN()
# ======================================================================================================================

try:
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
                optionDescriptionA()
                fname = input("First Name: ")
                lname = input("Last Name: ")

                randNum = random.randint(1, 999)
                randnumtostr = str(randNum)
                letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W',
                           'X', 'Y', 'Z']

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

                path = "C:/Users/User/OneDrive/Documents/Programming/Python_Projects/Python_Online_Voting_System/pseudodata/voterslist.txt"


                def verify_user(input_first, input_last, input_id):
                    try:
                        with open(path, "r") as file:
                            # Skip the header line (First Name   Last Name...)
                            next(file)

                            # Check every user row
                            for line in file:
                                # .split() breaks the line into a list of words, ignoring extra spaces
                                # Example: "John       Smith      ID123\n" -> ["John", "Smith", "ID123"]
                                parts = line.split()

                                # Safety check: make sure the line actually has 3 pieces of data
                                if len(parts) == 3:
                                    file_first = parts[0]
                                    file_last = parts[1]
                                    file_id = parts[2]

                                    # Check for an exact match (case-insensitive for names)
                                    if (file_first.lower() == input_first.lower() and
                                            file_last.lower() == input_last.lower() and
                                            file_id == input_id):
                                        return True  # Access Granted! Match found.

                    except FileNotFoundError:
                        print("Error: The user database file does not exist yet.")
                        return False

                    return False  # If the loop finishes without finding a match


                # --- Simulating the Sign-In Form ---
                print("--- MINI SIGN-IN FORM ---")
                entered_first = input("Enter First Name: ").strip()
                entered_last = input("Enter Last Name: ").strip()
                entered_id = input("Enter User ID: ").strip()

                if verify_user(entered_first, entered_last, entered_id):
                    print("\n✅ Access Granted! Welcome back.")
                    # Put the "something" they wanted to do right here!
                else:
                    print("\n❌ Access Denied! Incorrect Name or User ID.")

            case "C":
                print('C')

            case "D":
                optionDescriptionD()
                allowVisibility = ViewList()
                allowVisibility.showList()

            case "E":
                print('E')
                break

            case _:
                print("\nInvalid input.")

except KeyboardInterrupt:
    print("\n\n[!] Program interrupted by user. Exiting safely...")
except EOFError:
    print("\n\n[!] Unexpected end of input. Exiting safely...")
except PermissionError:
    print("\n[!] Error: Access denied to the database file. Please close it if it's open elsewhere.")
except IndexError:
    print("\n[!] Error: Data corruption detected in the voters list file formatting.")
except NameError as e:
    print(f"\n[!] Developer Error: A required function or module is missing: {e}")
except ValueError:
    print("Error: The user database file does not exist yet.")