class ViewCandidates:
    def __init__(self):
        # Update this path if necessary to match your project folder structure
        self.path = "C:/Users/HomePC/Downloads/project program/pycharm/Python_Online_Voting_System/pseudodata/candidatelist.txt"

    def print_ballot_layout(self):
        print("\n==================== CANDIDATE LIST =======================")
        print(f"Democratic Party             |           Republican Party")

        print("                        Presidential")
        print(f"[A]. Derek Hutchins          |           [B]. Avery De Mayo")

        print("                     Vice Presidential")
        print("[A]. Aurelia Vance           |           [B]. Evangeline Sinclair")

        print("                        Secretarial")
        print("[A]. Cyrus Sinclair          |           [C]. Cordelia Harrington")
        print("[B]. Meredith Kensington     |           [D]. Victoria Ashcroft")

        print("                         Treasurer")
        print("[A]. Lawrence Davenport      |           [C]. Atticus Blackwood")
        print("[B]. Leopold Thorne          |           [D]. Montgomery Pierce")

    def showCandidates(self):
        self.print_ballot_layout()