class UserScore:
    def __init__(self):
        self.users = []
        self.usersScore = {}

    def AddUser(self, user):
        self.users.append(user)
        score = 0
        self.usersScore[user] = score

    def AddScoreUser(self, user, addScore):
        score = addScore + self.usersScore[user]
        self.usersScore[user] = score

    def DeleteScoreUser(self, user, deleteScore):
        score = self.usersScore[user] - deleteScore
        self.usersScore[user] = score

    def DeleteUser(self, user):
        del self.usersScore[user]

    def ListUsers(self):
        users = []
        for user, score in self.usersScore.items():
            users.append(user)

        return users

    def UserScoreLists(self):
        return self.usersScore