class Register:
    def __init__(self, firstName, lastName, voterID):
        self.firstName = firstName
        self.lastName = lastName
        self.__voterID = voterID

    def showAndUpdateInfo(self):
        print(f"\nFirst Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Voter's Key/ID: {self.__voterID}")

        # PRIVATE ACCESS | NOT FOR VIEWING
        try:
            path = "C:/Users/User/OneDrive/Documents/Programming/Python_Projects/Python_Online_Voting_System/pseudodata/voterslist.txt"

            formatted_lines = []
            formatted_lines.append(f"{self.firstName:<12} {self.lastName:<12} {self.__voterID:<6}")
            with open(path, "a") as file:
                for line in formatted_lines:
                    file.write(line + "\n")
        except FileNotFoundError:
            print("Error: Database not found")

        # PUBLIC ACCESS | ONLY FOR VIEWING
        try:
            path = "C:/Users/User/OneDrive/Documents/Programming/Python_Projects/Python_Online_Voting_System/pseudodata/voterslistPRIVATE.txt"

            secretID = "****-***-*****"
            formatted_lines = []
            formatted_lines.append(f"{self.firstName:<12} {self.lastName:<12} {secretID:<6}")
            with open(path, "a") as file:
                for line in formatted_lines:
                    file.write(line + "\n")

            print("=============✔️=============")
        except FileNotFoundError:
            print("Error: Database not found")

        print("| 🟩 Voter Registered Successfully")