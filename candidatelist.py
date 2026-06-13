class ViewCandidates:
    def __init__(self):
        # Update this path if necessary to match your project folder structure
        self.path = "C:/Users/HomePC/Downloads/project program/pycharm/Python_Online_Voting_System/pseudodata/candidatelist.txt"

    def print_ballot_layout(self):
        print("\n========================= CANDIDATE LIST =========================")
        print(f"{'Democratic Party'.ljust(32)}| Republican Party")

        print(f"{''.ljust(14)}Presidential")
        print(f"{'[A]. Derek Hutchins'.ljust(32)}| [B]. Avery De Mayo")

        print(f"{''.ljust(11)}Vice Presidential")
        print(f"{'[A]. Aurelia Vance'.ljust(32)}| [B]. Evangeline Sinclair")

        print(f"{''.ljust(8)}Secretarial")
        print(f"{'[A]. Cyrus Sinclair'.ljust(32)}| [C]. Cordelia Harrington")
        print(f"{'[B]. Meredith Kensington'.ljust(32)}| [D]. Victoria Ashcroft")

        print(f"{''.ljust(5)}Treasurer")
        print(f"{'[A]. Lawrence Davenport'.ljust(32)}| [C]. Atticus Blackwood")
        print(f"{'[B]. Leopold Thorne'.ljust(32)}| [D]. Montgomery Pierce")

    def showCandidates(self):
        self.print_ballot_layout()