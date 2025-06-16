"""Quality management plan product stub."""

from ..Product import Product


class QualityManagementPlanProduct(Product):
    """Represents a quality management plan."""

    def __init__(self):
        super().__init__(
            name="QualityManagementPlanProduct",
            description="Describe quality assurance and control activities.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the quality management plan."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the quality management plan."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the quality management plan."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the quality management plan."""
        pass

