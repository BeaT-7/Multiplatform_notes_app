class Note():

    def __init__(self, noteID, groupID, noteName):
        self.id = int(noteID)
        self.group = int(groupID)
        self.name = noteName
        self.text = ""

    def getName(self):
        return self.name
