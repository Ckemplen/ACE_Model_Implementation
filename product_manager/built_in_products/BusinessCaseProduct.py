"""Business case product stub implementation."""

from ..Product import Product


class BusinessCaseProduct(Product):
    """Represents a simple business case document."""

    def __init__(self):
        super().__init__(
            name="BusinessCaseProduct",
            description="Compile a high level business case for the project.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the business case."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the business case."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the business case."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the business case to persistent storage."""
        pass

