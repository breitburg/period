class QuestionButton:
    def __init__(self, text, pictogram, action=None):
        self.text = text
        self.pictogram = pictogram
        self.action = action

    def activate(self):
        self.action()
