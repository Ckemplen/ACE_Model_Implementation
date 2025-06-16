"""Project approval documentation product stub."""

from ..Product import Product


class ProjectApprovalDocumentationProduct(Product):
    """Represents documentation for project approval."""

    def __init__(self):
        super().__init__(
            name="ProjectApprovalDocumentationProduct",
            description="Collate materials required for formal project approval.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the approval documentation."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the approval documentation."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize documentation for approval."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the approval documentation."""
        pass

