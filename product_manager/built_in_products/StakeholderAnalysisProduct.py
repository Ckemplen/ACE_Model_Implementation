"""Stakeholder analysis product stub."""

from ..Product import Product


class StakeholderAnalysisProduct(Product):
    """Represents a simple stakeholder analysis."""

    def __init__(self):
        super().__init__(
            name="StakeholderAnalysisProduct",
            description="Identify stakeholders and analyse their influence.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the stakeholder analysis."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the stakeholder analysis."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the stakeholder analysis."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the analysis."""
        pass

