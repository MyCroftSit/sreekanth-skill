from mycroft import MycroftSkill, intent_file_handler


class Sreekanth(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sreekanth.intent')
    def handle_sreekanth(self, message):
        self.speak_dialog('sreekanth')


def create_skill():
    return Sreekanth()

