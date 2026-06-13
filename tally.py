# tally.py

class TallySystem:
    def __init__(self):
        self.path = "C:/Users/HomePC/Downloads/project program/pycharm/Python_Online_Voting_System/pseudodata/tally.txt"

    def record_votes(self, voterID, pres, vp, sec, treas):
        """Saves all four position tokens securely onto a single row in the file."""
        try:
            if self.has_already_voted(voterID):
                print("\n🔴 Security Alert: You have already cast your ballot!")
                return False

            with open(self.path, "a") as file:
                # Store choices side-by-side separated by spaces
                file.write(f"{voterID} {pres} {vp} {sec} {treas}\n")
            return True
        except Exception as e:
            print(f"\n[!] Error writing tally data: {e}")
            return False

    def has_already_voted(self, voterID):
        try:
            with open(self.path, "r") as file:
                for line in file:
                    parts = line.split()
                    if parts and parts[0] == voterID:
                        return True
            return False
        except FileNotFoundError:
            return False

    def display_results(self):
        # Setup independent counters for each position tier
        pres_votes = {"A": 0, "B": 0}
        vp_votes = {"A": 0, "B": 0}
        sec_votes = {"A": 0, "B": 0, "C": 0, "D": 0}
        treas_votes = {"A": 0, "B": 0, "C": 0, "D": 0}

        try:
            with open(self.path, "r") as file:
                for line in file:
                    parts = line.split()
                    # A complete valid row must have 5 parts: VoterID, Pres, VP, Sec, Treas
                    if len(parts) == 5:
                        p, v, s, t = parts[1].upper(), parts[2].upper(), parts[3].upper(), parts[4].upper()

                        if p in pres_votes: pres_votes[p] += 1
                        if v in vp_votes: vp_votes[v] += 1
                        if s in sec_votes: sec_votes[s] += 1
                        if t in treas_votes: treas_votes[t] += 1
        except FileNotFoundError:
            pass

        print("\n========================= ELECTION TALLY RESULTS =========================")
        print(f"{'Democratic Party'.ljust(32)}| Republican Party")

        print(f"{''.ljust(14)}Presidential")
        print(f"{f'A. Derek Hutchins ({pres_votes.get('A', 0)} votes)'.ljust(32)}| B. Avery De Mayo ({pres_votes.get('B', 0)} votes)")

        print(f"{''.ljust(11)}Vice Presidential")
        print(f"{f'A. Aurelia Vance ({vp_votes.get('A', 0)} votes)'.ljust(32)}| B. Evangeline Sinclair ({vp_votes.get('B', 0)} votes)")

        print(f"{''.ljust(8)}Secretarial")
        print(f"{f'A. Cyrus Sinclair ({sec_votes.get('A', 0)} votes)'.ljust(32)}| C. Cordelia Harrington ({sec_votes.get('C', 0)} votes)")
        print(f"{f'B. Meredith Kensington ({sec_votes.get('B', 0)} votes)'.ljust(32)}| D. Victoria Ashcroft ({sec_votes.get('D', 0)} votes)")

        print(f"{''.ljust(5)}Treasurer")
        print(f"{f'A. Lawrence Davenport ({treas_votes.get('A', 0)} votes)'.ljust(32)}| C. Atticus Blackwood ({treas_votes.get('C', 0)} votes)")
        print(f"{f'B. Leopold Thorne ({treas_votes.get('B', 0)} votes)'.ljust(32)}| D. Montgomery Pierce ({treas_votes.get('D', 0)} votes)")
        print("==========================================================================")