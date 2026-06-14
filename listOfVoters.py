class ViewList:
    def showList(self):
        path = "C:/Users/User/OneDrive/Documents/Programming/Python_Projects/Python_Online_Voting_System/pseudodata/voterslistPRIVATE.txt"

        with open(path, "r") as file:
            print()
            content = file.read()
            print(content)