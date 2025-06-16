"""Capability to generate a user interaction plan."""

from ..Capability import Capability


class GenerateUserInteractionPlanCapability(Capability):
    """Stub that would plan system prompts and expected user responses."""

    def __init__(self):
        super().__init__(
            name="GenerateUserInteractionPlanCapability",
            description="Create an outline of planned interactions with the user.",
        )

    def execute(self):  # pragma: no cover - minimal stub
        """Execute generation of the interaction plan."""
        pass

