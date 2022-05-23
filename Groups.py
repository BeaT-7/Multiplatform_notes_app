class Group():

    def __init__(self, groupID, userID, groupName):
        self.id = int(groupID)
        self.owner = int(userID)
        self.name = groupName
        self.notes = []

    def appendNote(self, note):
        self.notes.append(note)

    def __len__(self):
        return len(self.notes)