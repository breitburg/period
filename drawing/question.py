class QuestionButton:
    def __init__(self, text, icon, action=None):
        self.text = text
        self.icon = icon
        self.action = action

    def activate(self):
        self.action()
