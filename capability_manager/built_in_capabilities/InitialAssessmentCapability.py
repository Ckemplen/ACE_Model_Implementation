from ..Capability import Capability
from .UserDialogueCapability import UserDialogueCapability

class InitialAssessmentCapability(Capability):
    def __init__(self):
        super().__init__(name="InitialAsessmentCapability",
                         description="Interact with the user to gather information and assess requirements.")

        self.more_information_required = True

    def execute(self):

        while self.more_information_required:
            self.gather_initial_information()
            self.estimate_required_resources_and_capabilities()
            self.test_understanding(user_input=UDC.question_user(self.generate_question()))

    def gather_initial_information(self):
        UDC = UserDialogueCapability()
        user_response, chat_history, chat_summary = UDC.question_user(self.generate_question())
        pass

    def estimate_required_resources_and_capabilities(self):
        # Use the gathered information to estimate required resources and capabilities
        # This method will likely need to be fleshed out with more specific logic
        pass

    def test_understanding(self, user_input):

        pass

    def generate_question(self):

        pass


if __name__ == "__main__":
    IAC = InitialAssessmentCapability()
    IAC.execute()
