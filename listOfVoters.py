class ViewList:
    def showList(self):
        path = "C:/Users/HomePC/Downloads/project program/pycharm/Python_Online_Voting_System/pseudodata/voterslistPRIVATE.txt"

        with open(path, "r") as file:
            print()
            content = file.read()
            print(content)