import random
import time
import sys

from listOfVoters import ViewList
from registerVoter import Register
from candidatelist import ViewCandidates
from tally import TallySystem

# FUNCTIONS
# ======================================================================================================================

def optionDescriptionA():
    print("\n------------- VOTER'S REGISTRATION FORM -------------")
    print("| Please fill in the necessary forms for registration.")

def optionDescriptionD():
    print("\n------------- REGISTERED VOTER'S LIST -------------")
    print("| The following is the list of people")
    print("| registered to vote.")

def optionDescriptionB():
    print("\n------------- CAST VOTE -------------")
    print("| Please enter your Name and Voter's Key/ID")
    print("| for validation.")

def effects(text, delay=0.1):
    """Prints text character by character with a specific delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Forces the character onto the screen immediately
        time.sleep(delay)
    print() # Moves to a new line once finished

candidate_viewer = ViewCandidates()
tally_manager = TallySystem()

# MAIN()
# ======================================================================================================================

try:
    while True:
        print("\nOnline Voting System")
        print("=============== ONLINE VOTING SYSTEM ===============")
        print("[A] ========== Register\n[B] ========== Cast Vote")
        print("[C] ========== View Candidate List\n[D] ========== View Registered Voters List")
        print("\n[E] ========== Show Results")
        print("\n[F] ========== Exit Program")

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
                print(f"\nYou Selected: {option}")
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
                optionDescriptionB()
                entered_first = input("Enter First Name: ").strip()
                entered_last = input("Enter Last Name: ").strip()
                entered_id = input("Enter User ID: ").strip()

                if verify_user(entered_first, entered_last, entered_id):
                    print(f"\n🟩 Access Granted! Welcome, {entered_first} {entered_last}!.")
                    # Put the "something" they wanted to do right here!

                    if tally_manager.has_already_voted(entered_id):
                        print("\n🔴 Security Alert: You have already cast your vote!")
                        continue

                    print("| Proceed...\n")

                    # Display layout once for baseline reference
                    candidate_viewer.print_ballot_layout()
                    print("=======================================================================")
                    print("\n--- BEGIN SEPARATE CATEGORY BALLOT VOTING ---")

                    # 1. PRESIDENTIAL SELECTION LOOP
                    while True:
                        print("\n[ Presidential Bracket Options: A or B ]")
                        p_choice = input("| Choose Presidential Candidate: ").strip().upper()
                        if p_choice in ["A", "B"]:
                            break
                        print("| Invalid selection. Please pick A or B for Presidential.")

                    # 2. VICE PRESIDENTIAL SELECTION LOOP
                    while True:
                        print("\n[ Vice Presidential Bracket Options: A or B ]")
                        vp_choice = input("| Choose Vice Presidential Candidate: ").strip().upper()
                        if vp_choice in ["A", "B"]:
                            break
                        print("| Invalid selection. Please pick A or B for Vice Presidential.")

                    # 3. SECRETARIAL SELECTION LOOP
                    while True:
                        print("\n[ Secretarial Bracket Options: A, B, C, or D ]")
                        sec_choice = input("| Choose Secretarial Candidate: ").strip().upper()
                        if sec_choice in ["A", "B", "C", "D"]:
                            break
                        print("| Invalid selection. Please pick A, B, C, or D for Secretarial.")

                    # 4. TREASURER SELECTION LOOP
                    while True:
                        print("\n[ Treasurer Bracket Options: A, B, C, or D ]")
                        treas_choice = input("| Choose Treasurer Candidate: ").strip().upper()
                        if treas_choice in ["A", "B", "C", "D"]:
                            break
                        print("| Invalid selection. Please pick A, B, C, or D for Treasurer.")

                    # Package and write the separate categories to tally data log
                    success = tally_manager.record_votes(entered_id, p_choice, vp_choice, sec_choice, treas_choice)
                    if success:
                        print("\n🟩 All category ballots recorded successfully! Voted Successfully!")

                else:
                    print("\n🔴 Incorrect Name or User ID.")

            case "C":
                print(f"\nYou Selected: {option}")
                candidate_viewer.showCandidates()

            case "D":
                print(f"\nYou Selected: {option}")
                optionDescriptionD()
                allowVisibility = ViewList()
                allowVisibility.showList()

            case "E":
                print(f"\nYou Selected: {option}")
                print("\n\nThe Moment of Truth...")
                print("\n" + "=" * 74)
                print("Fetching Results")
                effects("| #####", delay=0.5)
                print("Decrypting Ballot Box")
                effects("| #####", delay=0.5)
                print("Printing Winners")
                effects("| #####", delay=0.5)
                print("=" * 74)
                reveal = TallySystem()
                reveal.display_results()

            case "F":
                print(f"\nYou Selected: {option}")
                print("Closing Program...")
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
    print("\n[!] Error: Invalid Input Type entered.")