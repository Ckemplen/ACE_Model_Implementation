"""Communication plan product stub."""

from ..Product import Product


class CommunicationPlanProduct(Product):
    """Represents a basic communication plan."""

    def __init__(self):
        super().__init__(
            name="CommunicationPlanProduct",
            description="Outline project communication channels and frequency.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the communication plan."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the communication plan."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the communication plan."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the plan to persistent storage."""
        pass

