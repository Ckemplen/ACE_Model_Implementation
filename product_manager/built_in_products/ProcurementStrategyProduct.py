"""Procurement strategy product stub."""

from ..Product import Product


class ProcurementStrategyProduct(Product):
    """Represents a simple procurement strategy document."""

    def __init__(self):
        super().__init__(
            name="ProcurementStrategyProduct",
            description="Outline how required goods and services will be procured.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the procurement strategy."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the procurement strategy."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the procurement strategy."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the strategy."""
        pass

