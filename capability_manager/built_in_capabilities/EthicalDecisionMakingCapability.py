from ..Capability import Capability


class EthicalDecisionMakingCapability(Capability):
    """
    Ethical decision making capability.
    Either link to an external tool, or provide system messages etc for prompting LLMs
    """

    def __init__(self):
        super().__init__(
            name="EthicalDecisionMakingCapability",
            description="Perform basic ethical checks on proposed actions.",
        )

    def execute(self):
        """
        Execute the ethical decision making capability.
        """
        pass  # Implementation of the ethical decision making logic would go here
