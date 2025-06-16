"""Project scope statement product stub."""

from ..Product import Product


class ProjectScopeStatementProduct(Product):
    """Represents a brief statement of project scope."""

    def __init__(self):
        super().__init__(
            name="ProjectScopeStatementProduct",
            description="Define the scope and deliverables of the project.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the scope statement."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the scope statement."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the scope statement."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the scope statement."""
        pass

