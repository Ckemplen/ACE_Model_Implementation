"""Budget Proposal product stub."""

from ..Product import Product


class BudgetProposalProduct(Product):
    """Represents a simple budget proposal document."""

    def __init__(self):
        super().__init__(
            name="BudgetProposalProduct",
            description="Drafts a basic budget proposal for a project.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the budget proposal."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the budget proposal."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the budget proposal."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the proposal to persistent storage."""
        pass

