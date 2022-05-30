class Note():

    def __init__(self, noteID, groupID, noteName, text):
        self.id = int(noteID)
        self.group = int(groupID)
        self.name = noteName
        self.text = text
        self.size = (100, 140)

    def getName(self):
        return self.name
