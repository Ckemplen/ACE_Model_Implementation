"""Project schedule product stub."""

from ..Product import Product


class ProjectScheduleProduct(Product):
    """Represents a basic project schedule."""

    def __init__(self):
        super().__init__(
            name="ProjectScheduleProduct",
            description="Create a timeline of project activities.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the project schedule."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the project schedule."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the project schedule."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the schedule."""
        pass

