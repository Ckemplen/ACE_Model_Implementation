"""Project charter product stub."""

from ..Product import Product


class ProjectCharterProduct(Product):
    """Represents a basic project charter."""

    def __init__(self):
        super().__init__(
            name="ProjectCharterProduct",
            description="Summarize project objectives, scope and stakeholders.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the project charter."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the project charter."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the project charter."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the charter."""
        pass

