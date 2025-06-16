"""Resource plan product stub."""

from ..Product import Product


class ResourcePlanProduct(Product):
    """Represents a basic resource plan."""

    def __init__(self):
        super().__init__(
            name="ResourcePlanProduct",
            description="Plan for labour and material resources required.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the resource plan."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the resource plan."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the resource plan."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the plan."""
        pass

