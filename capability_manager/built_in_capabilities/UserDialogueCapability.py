from ..Capability import Capability


class UserDialogueCapability(Capability):
    def __init__(self):
        super().__init__(name="UserDialogue",
                         description="Basic capability class through which layers interact with the user.")

    def execute(self):
        pass

    def question_user(self, questions):
        #return user_response, chat_history, chat_summary
        pass


if __name__ == "__main__":
    UDC = UserDialogueCapability()
    UDC.execute()