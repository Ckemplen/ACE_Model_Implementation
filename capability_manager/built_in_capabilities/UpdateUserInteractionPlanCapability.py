"""Capability to update an existing user interaction plan."""

from ..Capability import Capability


class UpdateUserInteractionPlanCapability(Capability):
    """Stub for adjusting an existing interaction plan based on feedback."""

    def __init__(self):
        super().__init__(
            name="UpdateUserInteractionPlanCapability",
            description="Modify a previously generated user interaction plan.",
        )

    def execute(self):  # pragma: no cover - minimal stub
        """Apply updates to the interaction plan."""
        pass

